from django.shortcuts import render

# Create your views here.

from .models import Pet, Owner, Event, Breed

def index(request):
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
        'index.html',
        context={'num_owners':num_owners,'num_pet':num_pet,'num_breed':num_breed,'num_event':num_event},
    )
