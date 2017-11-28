from django import forms

class CreateNewEvent(forms.Form):
    start_time = forms.DateTimeField(help_text="Enter starting time in the form YYYY-MM-DD HH:MM:SS.")
    end_time = forms.DateTimeField(help_text="Enter the event ending timein the form YYYY-MM-DD HH:MM:SS.")
    description = forms.CharField()
    location = forms.CharField()
    