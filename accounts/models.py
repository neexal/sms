from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Grade(models.Model):
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.grade

        
class Student(models.Model):
    name=models.CharField(max_length=200)
    roll=models.IntegerField()
    symbolNo=models.CharField(max_length=10)
    grade =  models.ForeignKey(Grade, on_delete=CASCADE)

    def __str__(self):
        return self.name
    

class Exam(models.Model):
    TERMINAL=(
        ('First Terminal','First Terminal'),
        ('Second Terminal','Second Terminal'),
        ('Third Terminal', 'Third Terminal'),
    )
    year=models.CharField(max_length=10)
    terminal=models.CharField(max_length=50,choices=TERMINAL)

    def __str__(self):
        return self.year
    

class Subject(models.Model):
    subject=models.CharField(max_length=50)

    def __str__(self):
        return self.subject

class Mark(models.Model):
    # year= models.ForeignKey(Exam, on_delete=models.CASCADE,)
    subject= models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks=models.IntegerField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)


    # def __str__(self):
    #     return self.name
    

    