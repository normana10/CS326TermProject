from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.contrib.auth.models import Group

# Create your views here.
from .forms import *


from .models import Pet, Owner, Event, Breed, User
from .forms import FilterEventForm
from django.views.generic.edit import DeleteView
from django.core.urlresolvers import reverse_lazy

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

#@login_required
def dashboard(request):
    events=Event.objects.all()
    if request.user.is_authenticated():
        dogs=request.user.owner.pet_set.all()
    else:
        dogs=None
    if request.method == 'POST':
        form = FilterEventForm(request.POST)
        if form.is_valid():

            if not (form.cleaned_data.get('name') is None or form.cleaned_data.get('name')==""):
                print('filter name')
                events=events.filter(name__icontains=form.cleaned_data.get('name'))
            if not (form.cleaned_data.get('ownername') is None or form.cleaned_data.get('ownername')==""):
                print('filter ownername')
                events=events.filter(Q(host__user__username__icontains=form.cleaned_data.get('ownername'))
                    |Q(host__user__first_name__icontains=form.cleaned_data.get('ownername'))
                    |Q(host__user__last_name__icontains=form.cleaned_data.get('ownername')))
            if not form.cleaned_data.get('minstart') is None:
                print('minstart')
                events=events.filter(start_time__gte=form.cleaned_data.get('minstart'))
            if not form.cleaned_data.get('maxend') is None:
                print('maxend')
                events=events.filter(end_time__lte=form.cleaned_data.get('maxend'))

            #events=events.filter(Q(name__icontains=form.cleaned_data.get('name')),
            #    Q(host__user__username__icontains=form.cleaned_data.get('ownername'))
            #    |Q(host__user__first_name__icontains=form.cleaned_data.get('ownername'))
            #    |Q(host__user__last_name__icontains=form.cleaned_data.get('ownername')),
            #    Q(start_time__gte=form.cleaned_data.get('minstart')),
            #    Q(end_time__lte=form.cleaned_data.get('maxend'))
            #    )
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
    form = FilterEventForm(initial = {})
    return render(request,'find-event.html',{'form': form})

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
        form = NewEventForm(request.POST, request=request)

        if form.is_valid():
            eve = Event.objects.create(name = form.cleaned_data.get('name'),
                                        description = form.cleaned_data.get('description'),
                                        location = form.cleaned_data.get('location'),
                                        start_time = form.cleaned_data.get('start_time'),
                                        end_time = form.cleaned_data.get('end_time'),
                                        host = Owner.objects.all().filter(user_id=request.user.id)[0])
            return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = NewEventForm(request=request)
    return render(request, 'create-event.html', {'form': form})



def createpet(request):
    if request.method == 'POST':
        form = NewPetForm(request.POST)

        if form.is_valid():
            pet = Pet.objects.create(name = form.clean_name(), age = form.clean_age(), owner = Owner.objects.all().filter(user_id=request.user.id)[0], service = form.clean_service(), vaccinated = form.clean_vaccinated(), gender = form.clean_gender(), size = form.clean_size(), breed = [form.clean_breed()], disposition = form.clean_disposition(), additional_notes = form.clean_additional_notes())
            return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = NewPetForm(initial = {})
    return render(request, 'createpet.html', {'form': form})
class petDelete(DeleteView):
    model = Pet
    success_url = reverse_lazy('dashboard')


def createbreed(request):
    if request.method == 'POST':
        form = NewBreedForm(request.POST)

        if form.is_valid():
            breed = Breed.objects.create(breed = form.clean_breed())
            return HttpResponseRedirect(reverse('createpet'))

    else:
        form = NewBreedForm(initial = {})
    return render(request, 'createbreed.html', {'form': form})


from .forms import CreateAccountForm

def CreateAccount(request):

    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(
                    str(form.cleaned_data.get('username')),
                    str(form.cleaned_data.get('email')),
                    str(form.cleaned_data.get('password'))
                    )
            new_user.first_name = form.cleaned_data.get('first_name')
            new_user.last_name = form.cleaned_data.get('last_name')
            new_user.save()

            ourgroup=Group.objects.get(name='basicuser')
            ourgroup.user_set.add(new_user)

            return HttpResponseRedirect(reverse('dashboard'))

    else:
        form = CreateAccountForm(initial = {})

    return render(
            request,
            'create-account.html',
            {'form': form}
    )

from .forms import UpdateProfileForm
from .forms import UpdateProfileExtendedForm

@login_required
def UpdateProfile(request):

    user = request.user
    owner = user.owner

    if request.method == 'POST':
        # create a form instance and populate it with data from the request
        form_user = UpdateProfileForm(request.POST)
        form_extended = UpdateProfileExtendedForm(request.POST)

        if form_user.is_valid() and form_extended.is_valid():
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            user.email = request.POST['email']
            user.save()

            owner.gender = request.POST['gender']
            #owner.gender = request.POST['happiness']

            owner.save()
            return HttpResponseRedirect(reverse('dashboard'))

    else:
        u=Owner.objects.get(user=request.user)
        form_user = UpdateProfileForm(instance=u)
        form_extended = UpdateProfileExtendedForm(instance=u)


    return render(
            request,
            'update_profile_info.html',
            {'form_user': form_user,'form_extended': form_extended}
            )
