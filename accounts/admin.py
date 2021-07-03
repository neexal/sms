from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Subject)
admin.site.register(Mark)


