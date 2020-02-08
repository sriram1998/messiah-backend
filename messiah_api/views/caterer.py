from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View
import logging
import json

from ..models import Messes

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

        

        
        
        
       
