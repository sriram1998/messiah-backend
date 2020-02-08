from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
import logging
import json

from ..models import Student

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

        

        
        
        
       
