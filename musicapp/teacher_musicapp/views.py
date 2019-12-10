from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.template import loader
from .models import Member,Student,Teacher,Trackable,Recording,Note,IsStudentOf,Creates,IsAssigned
from django.db.models import Sum
from django import forms
from django.utils import timezone
from .forms import MyStudentForm


# Create your views here.


#THIS IS OUR CONTROLLER!!!!!!!!!!!
#semi handles routing (with urls.py)

#views are meant to take data from model (business logic) and return it to front end

def index(request):
    #this is checking how many students teacher_id 2
    query1 = IsStudentOf.objects.filter(teacher_id = 2).count()
    #this is checking the total duration of practice by student 1 on date 
    query2 = Recording.objects.filter(student = 1, day = '2019-01-01').aggregate(Sum('duration')).get('duration__sum')
    #this is checking the total duration of practice assigned to student 1 on date 
    query3 = IsAssigned.objects.filter(student_id = 1, practice_day = '2019-01-01').aggregate(Sum('time')).get('time__sum')
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
        'trackables': trackables,
        'recordings': recordings,
        'notes': notes,
        'query1':query1,
        'query2':query2,
        'query3':query3
    }
    return render(request, "teacher_musicapp/index.html", context)


def frontend(request):
    template = loader.get_template('teacher_musicapp/frontend.html') #load this specific tempalte
    return render(request, "teacher_musicapp/frontend.html")


def add_model(request):
    if request.method == "POST":
        form = MyStudentForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
    else:
        form = MyStudentForm()
        return render(request, "my_template.html", {'form': form})



def frontend2(request):

    users = Member.objects.all()
    students = Student.objects.all()
    teachers = Teacher.objects.all()
    trackables = Trackable.objects.all()
    recordings = Recording.objects.all()
    notes = Note.objects.all()
    query = Recording.objects.filter(student = 1, day = '2019-01-01').aggregate(Sum('duration')).get('duration__sum')


    template = loader.get_template('teacher_musicapp/frontend2.html') #load this specific template
    context = {
        'users': users,
        'students': students,
        'teachers': teachers,
        'trackables': trackables,
        'recordings': recordings,
        'notes': notes,
        'query': query
    }

    
    return render(request, "teacher_musicapp/frontend2.html", context)

def samson(request):
    template = loader.get_template('teacher_musicapp/samson.html') #load this specific tempalte
    return render(request, "teacher_musicapp/samson.html")