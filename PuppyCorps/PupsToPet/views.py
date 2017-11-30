from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

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

from .forms import UpdateUserInfoForm

def UpdateUserInfo(request):

    owner = get_object_or_404(Owner, pk = pk)
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding)
        form = UpdateUserInfoForm(request.POST)

        #Check if form is valid
        if form.is_valid():
            #process the data in form.cleaned_data as required 
            owner.first_name = form.cleaned_data['first_name']
            owner.last_name = form.cleaned_data['last_name']
            owner.email = form.cleaned_data['email']
            owner.gender = form.cleaned_data['gender']
            owner.save()

            #redirect to a new URL:
            return HttpResponseRedirect(reverse('dashboard'))

        #If this is a GET (or any other method) create the default form.
    else:
        form = UpdateUserInfoForm()

    return render(
            request, 
            'userinfo.html', 
            {'form': form}
        )

from .forms import NewAccountForm

def NewAccount(request):
    if request.method == 'POST':
        form = NewAccount(request.POST)    
        user = Owner.objects.create(first_name = form.fields['first_name'], last_name = form.fields['last_name'])
        return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = NewAccountForm(initial = {})
    
    return render(
            request, 
            'userinfocreateaccount.html', 
            {'form': form}
    )



