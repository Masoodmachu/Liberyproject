from django.contrib import admin
from student.models import Students
from student.models import Teacher
from student.models import CustomUser
# Register your models here.

admin.site.register(Students)
admin.site.register(Teacher)
admin.site.register(CustomUser)