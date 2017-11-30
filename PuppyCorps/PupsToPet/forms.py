from django import forms
from .models import Pet, Event
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class NewEventForm(forms.Form):
 
    eventName = forms.CharField()
    pets = forms.ModelMultipleChoiceField(Pet.objects.all())
    start_time = forms.CharField(help_text="Enter starting time in the form YYYY-MM-DD HH:MM.")
    end_time = forms.CharField(help_text="Enter the event ending timein the form YYYY-MM-DD HH:MM.")
    description = forms.CharField()
    location = forms.CharField()

class NewPetForm(forms.Form):
    pass
    name = forms.CharField()
    age = forms.IntegerField()
    service = forms.ChoiceField(choices=[('True','Yes'),('False','No')])
    vaccinated = forms.ChoiceField(choices=[('True','Yes'),('False','No')])
    gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')])
    size = forms.ChoiceField(choices=[('small','Small'),('medium','Medium'),('large','Large')])

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
    

 #   def CreateEvent(self):
 #       return Event.objects.create(name = eventName, pets = pets, start_time = start_time, end_time = end_time, description = description, location = location)

class NewAccountForm(forms.Form):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    gender = forms.ChoiceField(choices=[('M','Male'),('F','Female'), ('O', 'Space Bear')])
    profile_picture = forms.ImageField(required=False)

    def clean_first_name(self):
        data = self.cleaned_data['first_name']

        #Check that first name is at least 2 characters
        if len(data) < 2:
            raise ValidationError(_('Invalid first name. Must be at least two letters.'))

        #Check that first name is in range allowed and not more than 100 chars
        if len(data) >= 100:
            raise ValidationError(_('Invalid first name. Must be less than 100 letters.'))

        # Remember to always return the cleaned data.
        return data


    def clean_last_name(self):
        data = self.cleaned_data['last_name']

        #Check that last name is at least 2 characters
        if len(data) < 2:
            raise ValidationError(_('Invalid last name. Must be at least two letters.'))

        #Check that last name is in range allowed and not more than 100 chars
        if len(data) >= 100:
            raise ValidationError(_('Invalid last name. Must be less than 100 letters.'))

        # Remember to always return the cleaned data.
        return data

    def clean_email(self):
        data = self.cleaned_data['email']

        #Check that last name is at least 2 characters
        if len(data) < 1:
            raise ValidationError(_('Email field cannot be left blank.'))

        # Remember to always return the cleaned data.
        return data




class UpdateUserInfoForm(forms.Form):
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    gender = forms.ChoiceField(required=False, choices=[('M','Male'),('F','Female'), ('O', 'Space Bear')])
    profile_picture = forms.ImageField(required=False)









