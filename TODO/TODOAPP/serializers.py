from rest_framework import serializersfrom .models import *class StudentSerializer(serializers.ModelSerializer):    class Meta:        model = StudentModel        fields = ("id", "name", "roll", "section")