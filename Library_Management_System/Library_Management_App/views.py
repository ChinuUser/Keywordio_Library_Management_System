from django.shortcuts import render
from django.http import HttpResponse,HttpRequest

# Create your views here.

#def home_page_view(request):
    #return HttpResponse("Homepage")

def sign_page_view(request):
    return render(request,"Library_Manageent_App/Sign_Up.html")

def login_page_view(request):
    return render(request,"Library_Manageent_App/Login.html")

def landing_page_view(request):
    return render(request,"Library_Manageent_App/Landing_page.html")

def student_page_view(request):
    return render (request,"Library_Manageent_App/Student.html")

from rest_framework.views import APIView 
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer

class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer