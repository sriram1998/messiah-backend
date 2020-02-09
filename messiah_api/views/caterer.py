from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
import logging
from django.db.models import Count,Sum
import json
from django.http import HttpResponse




import datetime
from django.http import HttpResponse
from ..models import Student, Visited, Messes


from ..models import Messes, Menu, foodStats, Reviews

from .time_series import timeseries
from .food_predict import foodpredict  
class HttpResponseNoContent(HttpResponse):
    status_code = 404  
class LoginFormView(View):
    def post(self, request):
       
        mess = json.loads(request.body).get('messName')
        password = json.loads(request.body).get('password')
        
        try:
            user = Messes.objects.get(messName = mess, password = password)
            print(user)


            if user is not None:
                data = {'messID' : user.messID}
                return HttpResponse(json.dumps(data), content_type='application/json')

            
                
        except:        
            #return HttpResponse("invalid creds", content_type='application/json')
            return HttpResponseNoContent()
    

class studentAuthFormView(View):
    def post(self, request):
        messID = json.loads(request.body).get('messID') 
        date = json.loads(request.body).get('date')
        mealType = json.loads(request.body).get('mealType')
        studentID = json.loads(request.body).get('studentID')
        print(messID)
        print(json.loads(request.body))
        
        user = Student.objects.get(messID=messID, studentID=studentID)
        if user is not None:
            try:
                visited_check = Visited.objects.get(messID = messID, 
                                                   date = date,
                                                   mealType = mealType, 
                                                   studentID = studentID)
                
                return HttpResponse("You have already visited", content_type='application/json')

            except:
                mess = Messes.objects.get(messID = messID)

                Visited.objects.create(messID = mess, 
                                       date = date, 
                                       mealType = mealType, 
                                       studentID = user)
                return HttpResponse("verified", content_type='application/json')

        else:
            return HttpResponse("You have not registered to this mess", content_type='application/json')


class getStudentData(View):
    def post(self, request):
        mess = json.loads(request.body).get("messID")
        mealType1 = 'breakfast'
        mealType2 = 'lunch'
        mealType3 = 'dinner'
        print("hi",mess)
        students_list = []
        students_total = []
        studentsPerDate1 = Visited.objects.filter(mealType=mealType1).values('date').annotate(total=Count('studentID')).order_by('date')
        studentsPerDate2 = Visited.objects.filter(mealType=mealType2).values('date').annotate(total=Count('studentID')).order_by('date')
        studentsPerDate3 = Visited.objects.filter(mealType=mealType3).values('date').annotate(total=Count('studentID')).order_by('date')
        print("hey",len(studentsPerDate1))
        for i in range(0,len(studentsPerDate1)):
             students_list.append(studentsPerDate1[i])
             students_list.append(studentsPerDate2[i])
             students_list.append(studentsPerDate3[i])
             print(studentsPerDate2[i]['total'])
             students_total.append(studentsPerDate1[i]['total'])
             students_total.append(studentsPerDate2[i]['total'])
             students_total.append(studentsPerDate3[i]['total'])
        # return HttpResponse(students_total, content_type='application/json')
        print("works",students_total)
        resp = list(timeseries(students_total))
        print(resp)
        json_stuff = json.dumps({"response" : resp}) 
        return HttpResponse(json_stuff, content_type='application/json')
   

class foodConsumed(View):
    def post(self, request):

        date = json.loads(request.body).get("date")
        foodItem = json.loads(request.body).get("food")
        foodProd = json.loads(request.body).get("foodProd")
        foodLeft = json.loads(request.body).get("foodLeft")
        foodConsumed = int(foodProd) - int(foodLeft)
        try:
            
            food=Menu.objects.get(nameOfFood=foodItem)
           
            foodStats.objects.create(preparedQ = foodProd, consumedQ = foodConsumed, leftoverQ = foodLeft, date = date, menuID = food)
          
            return HttpResponse("data entered", content_type='text/plain')
        except Exception as e:
            return HttpResponse(e, content_type='text/plain')        

class getFoodData(View):
    def post(self, request):
        mess = json.loads(request.body).get("messID")
        mealType1 = 'breakfast'
        mealType2 = 'lunch'
        mealType3 = 'dinner'
        print("hi",mess)
        food_list = []
        food_total = []
        foodPerDate1 = foodStats.objects.filter().values('date').annotate(total=Sum('consumedQ')).order_by('date')
        print("hey",len(foodPerDate1))
        for i in range(0,len(foodPerDate1)):
             food_list.append(foodPerDate1[i])
             print(foodPerDate1[i]['total'])
             food_total.append(foodPerDate1[i]['total'])
        print("works",food_total)
        resp = list(foodpredict(food_total))
        print(resp)
        json_stuff = json.dumps({"response" : resp}) 
        return HttpResponse(json_stuff, content_type='application/json')

class viewComplaints(View):
    def post(self, request):
        messID = json.loads(request.body).get("messID")
        reviews_list=[]
        print(messID)
        p=Messes.objects.get(messID=messID)
        review_arr=Reviews.objects.filter(messID=p)
        for i in review_arr:
            reviews_list.append(i.review)
            print(i.review)
        resp = list(reviews_list)
        print(resp)
        print(reviews_list)
        json_stuff = json.dumps({"response" : resp})
        return HttpResponse(json_stuff, content_type='text/plain')
       
