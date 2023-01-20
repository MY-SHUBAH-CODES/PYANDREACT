from.models import *
from rest_framework import serializers

class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields=['id','name','age','roll_number']
        