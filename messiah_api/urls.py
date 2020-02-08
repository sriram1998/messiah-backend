from django.urls import path, include
from django.conf.urls import url
from django.views.generic import RedirectView

#from .views import user
from .views import user,caterer
urlpatterns = [
    url('user/login', user.LoginFormView.as_view()),
    url('caterer/login', caterer.LoginFormView.as_view()),
    url('user/menu', user.MenuView.as_view()),
    url('user/allMenu', user.allMenuView.as_view()),
    url('caterer/studentAuth', caterer.studentAuthFormView.as_view()),
    url('user/review', user.review.as_view()),
    url('caterer/getStudentData', caterer.getStudentData.as_view())

]

