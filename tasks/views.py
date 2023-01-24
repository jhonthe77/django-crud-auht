from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')


def signup(request):
    print(request.POST)
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'errors': 'Username already exists'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'errors': 'password does not match'
        })

def tasks(request):
    return render(request, 'task.html')

def signupout(request):
    logout(request)
    return redirect('home')

def signin(request):
    return render(request, 'signin.html',{
        'from': AuthenticationForm
    })