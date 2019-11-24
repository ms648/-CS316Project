from django.contrib import admin
from .models import Member,Student,Teacher,Trackable,Recording,Note,IsStudentOf,Creates,IsAssigned
# Register your models here.
admin.site.register(Member)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Trackable)
admin.site.register(Recording)
admin.site.register(Note)
admin.site.register(IsStudentOf)
admin.site.register(Creates)
admin.site.register(IsAssigned)

