from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
import logging
import json



import datetime

from ..models import Student
from ..models import Messes
from ..models import Visited

class LoginFormView(View):
    def post(self, request):
       
        mess = request.POST.get('messName')
        password = request.POST.get('password')
        
        try:
            user = Messes.objects.get(messName = mess, password = password)

            if user is not None:
                data = {'messName' : user.messName}
                return HttpResponse(json.dumps(data), content_type='text/plain')

            
                
        except:        
            return HttpResponse("invalid creds", content_type='text/plain')

        

        
        
        
       


class studentAuthFormView(View):
    def post(self, request):
        messID = request.POST.get('messID') 
        date = request.POST.get('date')
        mealType = request.POST.get('mealType')
        studentID = request.POST.get('studentId')
        print(messID)
        
        user = Student.objects.get(messID=messID, studentID=studentID)
        if user is not None:
            try:
                visited_check = Visited.objects.get(messID = messID, 
                                                   date = date,
                                                   mealType = mealType, 
                                                   studentID = studentID)
                
                return HttpResponse("You have already visited", content_type='text/plain')

            except:
                mess = Messes.objects.get(messID = messID)

                Visited.objects.create(messID = mess, 
                                       date = date, 
                                       mealType = mealType, 
                                       studentID = user)
                return HttpResponse("verified", content_type='text/plain')

        else:
            return HttpResponse("You have not registered to this mess", content_type='text/plain')





