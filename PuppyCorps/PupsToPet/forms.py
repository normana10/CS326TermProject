from django import forms
from .models import Pet, Event

class NewEventForm(forms.Form):


    
    eventName = forms.CharField()
    pets = forms.ModelMultipleChoiceField(Pet.objects.all())
    start_time = forms.DateTimeField(help_text="Enter starting time in the form YYYY-MM-DD HH:MM.")
    end_time = forms.DateTimeField(help_text="Enter the event ending timein the form YYYY-MM-DD HH:MM.")
    description = forms.CharField()
    location = forms.CharField()

 #   def CreateEvent(self):
 #       return Event.objects.create(name = eventName, pets = pets, start_time = start_time, end_time = end_time, description = description, location = location)