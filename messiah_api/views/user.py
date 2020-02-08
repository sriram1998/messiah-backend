from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
import logging

from ..models import User 

class LoginFormView(View):
    def post(self, request):
       
        roll = request.POST.get('roll')
        password = request.POST.get('password')
        
        user = User.objects.get(roll_number = roll, password = password)
        



        if user is not None:
            return HttpResponse(user.roll_number, content_type='text/plain')

        else:
            return HttpResponse("invalid creds", content_type='text/plain')

        
        
        #return HttpResponse(user.roll_number, content_type='text/plain')
