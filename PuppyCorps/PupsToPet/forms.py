from django import forms
from .models import Pet, Event

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
    owner = 12345
    service = forms.BooleanField()
    vaccinated = forms.BooleanField()
    gender = forms.ChoiceField(choices=[('Male','Male'),('Female','Female')])
    size = forms.ChoiceField(choices=[('small','Small'),('medium','Medium'),('large','Large')])

 #   def CreateEvent(self):
 #       return Event.objects.create(name = eventName, pets = pets, start_time = start_time, end_time = end_time, description = description, location = location)