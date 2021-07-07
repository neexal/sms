from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(Subject)

admin.site.register(Grade)

class MarkAdmin(admin.ModelAdmin):
	list_display = ('id','subject', 'student','marks',)
	search_fields = ('student',)
	list_display_links = ('id','student', )
admin.site.register(Mark, MarkAdmin)


