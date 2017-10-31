from django.shortcuts import render
from .models import Pet, Owner, Event, Breed

# Create your views here.

def index(request):
    return render(
        request,
        'index.html',
    )
    
def dashboard(request):
    return render(
        request,
        'dashboard.html',
    )
    
def createaccount(request):
    return render(
        request,
        'create-account.html',
    )
    
def login(request):
    return render(
        request,
        'log-in.html',
    )
    
def forgotpassword(request):
    return render(
        request,
        'forgot-password.html',
    )
    
def createevent(request):
    return render(
        request,
        'create-event.html',
    )
    
def findevent(request):
    return render(
        request,
        'find-event.html',
    )
    
def userinfo(request):
    return render(
        request,
        'userinfo.html',
    )
    
def doginfo(request):
    return render(
        request,
        'dog-info.html',
    )
    
def vomit(request):
    events=Event.objects.all()
    return render(
        request,
        'list-vomit.html',
        context={'events':events},
    )