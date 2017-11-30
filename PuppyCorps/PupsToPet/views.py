from django.shortcuts import render

# Create your views here.

from .models import Pet, Owner, Event, Breed

def about(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    events=Event.objects.all()
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
        context={'events':events},
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
    
#def createevent(request):
#    return render(
#        request,
#       'create-event.html',
#    )
    
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

from .forms import NewEventForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def createevent(request):
    if request.method == 'POST':
        form = NewEventForm(request.POST)
        
        if form.is_valid():
            eve = Event.objects.create(name = form.cleaned_data.get('name'), description = form.cleaned_data.get('description'), location = form.cleaned_data.get('location'))
            return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = NewEventForm(initial = {})
    return render(request, 'create-event.html', {'form': form})
    
