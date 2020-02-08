from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
import logging
import json

from ..models import Student,Menu

class LoginFormView(View):
    def post(self, request):
       
        roll = request.POST.get('roll')
        password = request.POST.get('password')
        
        try:
            user = Student.objects.get(rollNo = roll, password = password)
        
            if user is not None:
                data = {'rollNum' : user.rollNo, 'mess' : user.messID.messName, 'name' : user.name}
                return HttpResponse(json.dumps(data), content_type='text/plain')
            
        except:        
            return HttpResponse("invalid creds", content_type='text/plain')

class MenuView(View):
    def post(self, request):
       
        messID = request.POST.get('messID')
        day = request.POST.get('day')
        meal = request.POST.get('mealType')
        try:
            menu = Menu.objects.filter(messID=messID,day=day,mealType=meal)

            if menu is not None:
                response=str(menu[0].nameOfFood)
                for i in range(1,len(menu)):
                    response=response+","+str(menu[i].nameOfFood)
                data = {'menu' : response}
                return HttpResponse(json.dumps(data), content_type='text/plain')

        except:        
            return HttpResponse("invalid creds", content_type='text/plain')


        

        
        
        
       
