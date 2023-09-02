from django.contrib import admin
from .models import Student
from .models import Attendance
from .models import ImageStore
# Register your models here.

admin.site.register(Student)
admin.site.register(Attendance)
admin.site.register(ImageStore)