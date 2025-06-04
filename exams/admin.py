from django.contrib import admin
from .models import User, Student, Exam, ExamHall, HallAllocation

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Exam)
admin.site.register(ExamHall)
admin.site.register(HallAllocation)
