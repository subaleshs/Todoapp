from django import forms
from django.http import request
from django.shortcuts import render,redirect
from .models import todo
from django.views.decorators.http import require_http_methods
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import registerForm
from django.contrib.auth.models import User


def home(request):
    if request.method == 'POST': # When user logs in 
        un = request.POST['username']
        ps = request.POST['password']
        user = authenticate(username=un, password=ps)
        if user:
            login(request,user)
            jobs = todo.objects.filter(usrid=user.id)
            return render(request,'tapp/todofr.html',{'jobs':jobs})
        else:
            return render(request,'tapp/todofr.html',{'msg':'INVALID CREDENTIALS'})
    elif request.user: #redirected to home
        jobs = todo.objects.filter(usrid=request.user.id)
        return render(request,'tapp/todofr.html',{'jobs':jobs})

    else:
        return render(request,'tapp/todofr.html')

#ADD a new job to todo list
@require_http_methods(['POST'])
def newJob(request):
    usr = request.user
    print(usr)
    job = request.POST['td']
    new_job = todo.objects.create(job=job,usrid=usr)
    new_job.save()
    return redirect(home)

def deleteJob(request,jid):
    usr = request.user
    job = todo.objects.get(pk=jid,usrid=usr)
    job.delete()
    return redirect(home)

#Mark a job as completed

def jobDone(request,jid):
    usr = request.user
    job = todo.objects.get(pk=jid,usrid=usr)
    job.stat = True
    job.save()
    return redirect(home)

#Mark a job as not completed

def notDone(request,jid):
    usr = request.user
    job = todo.objects.get(pk=jid,usrid=usr)
    job.stat = False
    job.save()
    return redirect(home)

#new user registration

def register(request):
    if request.method == 'POST':
        frmData = registerForm(request.POST)
        print(frmData.errors)
        if frmData.is_valid():
            frmData.save()
            return redirect(home)
        else:
            form = registerForm()
            return render(request,'tapp/register.html',{'form':form,'msg':frmData.errors})   
    else:
        form = registerForm()
        return render(request,'tapp/register.html',{'form':form})