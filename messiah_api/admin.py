from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Messes)
admin.site.register(Student)
admin.site.register(Menu)
admin.site.register(foodStats)
admin.site.register(Visited)
admin.site.register(Reviews)
#admin.site.register(FeedBack)