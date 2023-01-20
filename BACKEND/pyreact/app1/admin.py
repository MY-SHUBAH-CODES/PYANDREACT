from django.contrib import admin
from .models import *

class Studentadmin(admin.ModelAdmin):
    list_display=['id','name','age','roll_number']
admin.site.register(Student,Studentadmin)


