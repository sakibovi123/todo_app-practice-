from django.shortcuts import render
from django.http import JsonResponse
from .serializers import  StudentSerializer
from rest_framework.views import APIView
from .models import StudentModel
from rest_framework.response import Response
from rest_framework import status

class IndexView(APIView):
    def get(self, request):
        queryset = StudentModel.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)


class CreateStudentView(APIView):
    def post(self, request):
        data = request.data
        name = data["name"]
        roll = data["roll"]
        section = data["section"]

        if name and roll and section:
            StudentModel.objects.create(
                name=name,
                roll=roll,
                section=section,
            )
            return Response(status=status.HTTP_201_CREATED)

