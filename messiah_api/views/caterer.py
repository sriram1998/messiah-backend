from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
import logging
from django.db.models import Count
import json
from django.http import HttpResponse



import datetime
from django.http import HttpResponse
from ..models import Student, Visited, Messes


from ..models import Messes, Menu, foodStats, Reviews

from .time_series import timeseries 
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
        date = json.loads(request.body).get("date")
        students_list = []
        students_total = []
        studentsPerDate = Visited.objects.filter(date=date).values('mealType').annotate(total=Count('studentID')).order_by('mealType')
        print(studentsPerDate)
        
        for i in studentsPerDate:
             students_list.append(i)
             print(i['total'])
             students_total.append(i['total'])
        # return HttpResponse(students_total, content_type='application/json')
        print(students_total)
        
        return HttpResponse(timeseries(students_total), content_type='application/json')
   

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

class viewComplaints(View):
    def post(self, request):
        messID = json.loads(request.body).get("messID")
        reviews_list=[]
        p=Messes.objects.get(messID=messID)
        review_arr=Reviews.objects.filter(messID=p)
        for i in review_arr:
            reviews_list.append(i)
            print(i.review)
        
        return HttpResponse("done", content_type='text/plain')
       
