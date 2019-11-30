from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from .models import Member,Student,Teacher,Trackable,Recording,Note,IsStudentOf,Creates,IsAssigned


# Create your views here.


#THIS IS OUR CONTROLLER!!!!!!!!!!!
#semi handles routing (with urls.py)

#views are meant to take data from model (business logic) and return it to front end

def index(request):
    #this is checking how many students teacher_id 2
    query1 = IsStudentOf.objects.filter(teacher_id = 2).count()
    users = Member.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    trackables = Trackable.objects.all()
    recordings = Recording.objects.all()
    notes = Note.objects.all()

    # IsStudentOf = IsStudentOf.objects.all()
    # Creates = Creates.objects.all()
    # IsAssigned = IsAssigned.objects.all()
    template = loader.get_template('teacher_musicapp/index.html') #load this specific tempalte
    context = {
        'users': users,
        'students': students,
        'teachers': teachers,
        'students': students,
        'trackables': trackables,
        'recordings': recordings,
        'notes': notes,
        'query1':query1
    }
    return render(request, "teacher_musicapp/index.html", context)


def frontend(request):
    template = loader.get_template('teacher_musicapp/frontend.html') #load this specific tempalte
    return render(request, "teacher_musicapp/frontend.html")
