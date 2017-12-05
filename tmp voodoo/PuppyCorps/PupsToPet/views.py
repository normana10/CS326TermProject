from django.shortcuts import render

# Create your views here.

from .models import Pet, Owner, Event, Breed
from django.contrib.auth.models import User
from .forms import CreateUserForm

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

def about(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_owners = Owner.objects.all().count()
    num_breed = Breed.objects.all().count()
    num_pet = Pet.objects.all().count()
    num_event = Event.objects.all().count()
    # Available books (status = 'a')
    #num_instances_available=BookInstance.objects.filter(status__exact='a').count()
    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'about-page.html',
        context={'events':Event.objects.all()},
    )

def dashboard(request):
    events=Event.objects.all()
    if request.user.is_authenticated():
        dogs=request.user.owner.pet_set.all()
    else:
        dogs=None
    return render(
        request,
        'dashboard.html',
        context={'events':events,'dogs':dogs},
    )
    
def createaccount(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            newuser = User.objects.create_user(str(form.cleaned_data['username']),str(form.cleaned_data['email']),str(form.cleaned_data['password1']))
            newuser.first_name = form.cleaned_data['firstname']
            newuser.last_name = form.cleaned_data['lastname']
            newuser.save()
            return HttpResponseRedirect(reverse('about'))
    else:
        form = CreateUserForm(initial={'username': 'tmp','password1': 'tmp','password2': 'tmp','firstname': 'tmp','lastname': 'tmp','email': 'tmp@tmp.com',})
    return render(request,'create-account.html',{'form':form})
    
#def login(request):
#    return render(
#        request,
#        'log-in.html',
#    )
    
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

def test(request):
    return render(
        request,
        'test.html',
    )