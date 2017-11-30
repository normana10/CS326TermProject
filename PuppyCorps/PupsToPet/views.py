from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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

@login_required
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

def createevent(request):
    if request.method == 'POST':
        form = NewEventForm(request.POST)
        
        eve = Event.objects.create(name = form.fields['eventName'], start_time = form.fields['start_time'], end_time = form.fields['end_time'], description = form.fields['description'], location = form.fields['location'])
        return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = NewEventForm(initial = {})
    return render(request, 'create-event.html', {'form': form})
    

from .forms import NewPetForm

def createpet(request):
    if request.method == 'POST':
        form = NewPetForm(request.POST)
        
        pet = Pet.objects.create(name = form.clean_name(), age = form.clean_age(), owner = Owner.objects.all().filter(user_id=request.user.id)[0], service = form.clean_service(), vaccinated = form.clean_vaccinated(), gender = form.clean_gender(), size = form.clean_size())
        return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = NewPetForm(initial = {})
    return render(request, 'createpet.html', {'form': form})
    
