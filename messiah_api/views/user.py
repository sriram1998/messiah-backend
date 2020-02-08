from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
import logging
import json

from ..models import Student,Menu,Reviews,Messes  

class LoginFormView(View):
    def post(self, request):
       
        roll = json.loads(request.body).get('roll')
        password = json.loads(request.body).get('password')
        
        try:
            user = Student.objects.get(rollNo = roll, password = password)
        
            if user is not None:
                data = {'rollNum' : user.rollNo, 'mess' : user.messID.messName, 'name' : user.name}
                return HttpResponse(json.dumps(data), content_type='application/json')
            
        except Exception as e:
            return HttpResponse(e, content_type='text/plain')

class MenuView(View):
    def post(self, request):
       
        messID = json.loads(request.body).get('messID')
        day = json.loads(request.body).get('day')
        meal = json.loads(request.body).get('mealType')
        try:
            menu = Menu.objects.filter(messID=messID,day=day,mealType=meal)

            if menu is not None:
                response=str(menu[0].nameOfFood)
                for i in range(1,len(menu)):
                    response=response+","+str(menu[i].nameOfFood)
                data = {'menu' : response}
                return HttpResponse(json.dumps(data), content_type='application/json')

        except:        
            return HttpResponse("invalid creds", content_type='application/json')


class allMenuView(View):
    def post(self, request):

        messid = json.loads(request.body).get('messID')
        day=json.loads(request.body).get('day')
        mealType=json.loads(request.body).get('mealType')
        print(messid)
        print(day)
        print(mealType)
        try: 
            menu = list(Menu.objects.filter(messID = messid,day=day,mealType=mealType).values_list('nameOfFood'))
            m=''
            print(len(messid))
            
            for i in range(len(menu)):
                menu[i]=list(menu[i])
            for i in range(len(menu)):
                m+=menu[i][0]+','+'\n'
            print(m)

            return HttpResponse(m, content_type='application/json')

        except:        
            return HttpResponse("invalid", content_type='application/json')

class review(View):
    def post(self, request):
        
        messid = json.loads(request.body).get('messid')
        feedbackText = json.loads(request.body).get('feedbackText')
        mess = Messes.objects.get(messID=messid)
        try:
            Reviews.objects.create(messID = mess, review = feedbackText)
            return HttpResponse("data entered", content_type='text/plain')
        except Exception as e:
            return HttpResponse(e, content_type='text/plain')




       
