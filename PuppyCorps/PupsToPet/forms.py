from django import forms
from .models import Pet, Event, Owner, Breed
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm
from datetimewidget.widgets import DateTimeWidget
import re
from django.contrib.auth.models import User


class NewEventForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super(NewEventForm, self).__init__(*args, **kwargs)
        currentOwner = Owner.objects.all().filter(user=self.request.user)
        # self.fields['host'] = currentOwner
        # self.fields['pets'] = forms.ModelMultipleChoiceField(Pet.objects.all().filter(owner=currentOwner))
        if len(Pet.objects.all().filter(owner=currentOwner)) == 0:
            self.fields['pets'] = forms.MultipleChoiceField([("You have no pets.","You have no pets.")])
        else:
            self.fields['pets'] = forms.ModelMultipleChoiceField(Pet.objects.all().filter(owner=currentOwner))

    name = forms.CharField()
#    pets = forms.ModelMultipleChoiceField(Pet.objects.all())
    start_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    end_time = forms.DateTimeField(widget=DateTimeWidget(usel10n=True, bootstrap_version=3))
    description = forms.CharField()
    location = forms.CharField()

    def clean(self):
        print(self.request.user)

    def clean_name(self):
        return self.cleaned_data['name']

    def clean_description(self):
        return self.cleaned_data['description']

    def clean_start_time(self):
        return self.cleaned_data['start_time']

    def clean_end_time(self):
        return self.cleaned_data['end_time']


class NewPetForm(forms.Form):
    name = forms.CharField(label="Your pet's name")
    age = forms.IntegerField(label="Your pet's age")
    service = forms.ChoiceField(choices=[('True','Yes'),('False','No')],label="Is your pet a service animal?")
    vaccinated = forms.ChoiceField(choices=[('True','Yes'),('False','No')], label="Is your pet vaccinated?")
    gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')], label="What is your pet's gender?")
    size = forms.ChoiceField(choices=[('small','Small'),('medium','Medium'),('large','Large')], label="What is your pet's size?")
    breed = forms.ModelChoiceField(Breed.objects.order_by('breed'), label="What breed is your pet? ")

    disposition = forms.CharField(label="What is your pet like? Choose from the options below. Choose one or many! Or start typing and the disposition will show up (ex: happy, sad, energetic, etc)")
    additional_notes = forms.CharField(required="False", label="Is there anything else we should know about your pet? Write it down below!")

    def clean_name(self):
        data = self.cleaned_data['name']
        return data
    def clean_age(self):
        data = self.cleaned_data['age']
        return data
    def clean_service(self):
        data = self.cleaned_data['service']
        return data
    def clean_vaccinated(self):
        data = self.cleaned_data['vaccinated']
        return data
    def clean_gender(self):
        data = self.cleaned_data['gender']
        return data
    def clean_size(self):
        data = self.cleaned_data['size']
        return data
    def clean_breed(self):
        data = self.cleaned_data['breed']
        return data
    def clean_disposition(self):
        data = self.cleaned_data['disposition']
        return data
    def clean_additional_notes(self):
        data = self.cleaned_data['additional_notes']
        return data


    def clean(self):
        age = self.cleaned_data['age']

        if (age < 0):
            raise ValidationError(_('Error: Invalid age! It cannot be a negative number!'))

class NewBreedForm(forms.Form):
    breed = forms.CharField(label="Your New Breed!")

    def clean_breed(self):
        data = self.cleaned_data['breed']
        return data


 #   def CreateEvent(self):
 #       return Event.objects.create(name = eventName, pets = pets, start_time = start_time, end_time = end_time, description = description, location = location)

class CreateAccountForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Please enter a valid username. No spaces and at least 6 to 25 characters.'})
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.ChoiceField(
            choices=[(
            'M','Male'),
            ('F','Female'),
            ('SB', 'Space Bear')
            ])
    email = forms.EmailField()
    password = forms.CharField( widget=forms.PasswordInput() )
    confirm_password= forms.CharField( widget=forms.PasswordInput() )
    #profile_picture = forms.ImageField(label='Upload a profile picture!', required=False)


    def clean_username(self):
        username = self.cleaned_data["username"]
        return username

    def clean_first_name(self):
        firstname = self.cleaned_data['first_name']
        return firstname

    def clean_last_name(self):
        lastname = self.cleaned_data['last_name']
        return lastname

    def clean_email(self):
        email_passed = self.cleaned_data['email']
        return email_passed

    def clean_gender(self):
        gender = self.cleaned_data['gender']
        return gender

    def clean_password(self):
        password = self.cleaned_data['password']
        return password

    def clean_confirm_password(self):
        confirmed_pwd = self.cleaned_data['confirm_password']
        return confirmed_pwd

    #def clean_profile_picture(self):
     #   picture_passed = self.cleaned_data['profile_picture']
      #  return picture_passed

    def clean(self):
        password = self.cleaned_data['password']
        confirmed_password = self.cleaned_data['confirm_password']
        firstname = self.cleaned_data['first_name']
        lastname = self.cleaned_data['last_name']
        username = self.cleaned_data['username']

        # Check that username is not already taken
        #if User.objects.filter(username.exists()):
         #   raise ValidationError(_('Error: Username is already taken.'))

        if (len(username) < 6):
            raise ValidationError(_('Error: Username is too short. Must be between 6 to 25 characters.'))

        if (len(username) > 25):
            raise ValidationError(_('Error: Username is too long. Must be between 6 to 25 characters.'))

        if (re.search(r"\s", str(username))):
            raise ValidationError(_('Error: Username cannot contain spaces.'))

        if (any(char.isdigit() for char in str(username)) != True):
            raise ValidationError(_('Error: Username must contain at least 1 number.'))

        if (password != confirmed_password):
            raise ValidationError(_('Error: Passwords do not match.'))

        if (len(password) < 6):
            raise ValidationError(_('Error: Password is too short. Must contain at least 6 characters'))

        if (any(char.isdigit() for char in str(password)) != True):
            raise ValidationError(_('Error: Password must contain at least 1 number.'))

        if (str(firstname.lower()) in str(password).lower()):
            raise ValidationError(_('Error(101): Password cannot contain your name/username.'))

        if (str(lastname.lower()) in str(password).lower()):
            raise ValidationError(_('Error(102): Password cannot contain your name/username.'))

        if (str(username.lower()) in str(password).lower()):
            raise ValidationError(_('Error(103): Password cannot contain your name/username.'))

class UpdateProfileForm(forms.ModelForm):
# When a user creates an account, prefill this form with that info.
# When a user updates this form, update their info & make sure it stays in this form when the user views it.
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        return data

    def clean_email(self):
        data = self.cleaned_data['email']
        return data

    def clean(self):
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']

        if (len(first_name) == 1):
            raise ValidationError(_('Error: Your first name cannot just contain 1 letter.'))
        if (len(last_name) == 1):
            raise ValidationError(_('Error: Your last name cannot just contain 1 letter.'))

        if (any(char.isdigit() for char in str(firstname)) != False):
            raise ValidationError(_('Error: Your first name may not contain any numbers'))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UpdateProfileExtendedForm(forms.ModelForm):

    def clean_gender(self):
        data = self.cleaned_data['gender']
        return data

   # def clean_happiness(self):
    #    data = self.cleaned_data['happiness']
     #   return data

    #def clean_happiness(self):
    #    data = self.cleaned_data['happiness']

   # def clean_hobbies(self):
    #    data = self.cleaned_data['hobbies']


    #def clean_profile_picture(self):
     #   data = self.cleaned_data['profile_picture']

    class Meta:
        model = Owner
 #       fields = ['gender', 'hobbies', 'profile_picture']
        fields = ['gender']
