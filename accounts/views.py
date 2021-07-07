from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.
def home(request):
    context = {
        'classes' : Grade.objects.all(),
        'subjects' : Subject.objects.all(),
    }
    if request.method == 'POST' and 'createResult' in request.POST:
        grade = request.POST["grade"]
        subject =  request.POST['subject']
        context = {
            'students' : Student.objects.filter(grade=grade),
            'subjects' : Subject.objects.filter(id=subject),
        }
        return render(request,'accounts/students.html', context) 

    if request.method == 'POST' and 'addMarks' in request.POST:
        marks =  request.POST['marks']
        student = request.POST['student']
        subject = request.POST['subject']
        new_data = Mark.objects.create(subject_id=subject,marks=marks,student_id=student).save()

        return render(request,'accounts/students.html', context) 


    return render(request,'accounts/dashboard.html', context)

def student(request):
    pass