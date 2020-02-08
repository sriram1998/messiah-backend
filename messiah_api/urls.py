from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView

#from .views import user
from .views import user
urlpatterns = [
    url('user/login', user.LoginFormView.as_view()),
]