from django import forms
from .models import Pet, Event, Owner
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import ModelForm



class NewEventForm(forms.Form):
 
    name = forms.CharField()
    pets = forms.ModelMultipleChoiceField(Pet.objects.all())
    start_time = forms.DateTimeField(help_text="Enter starting time in the form YYYY-MM-DD HH:MM.")
    end_time = forms.DateTimeField(help_text="Enter the event ending timein the form YYYY-MM-DD HH:MM.")
    description = forms.CharField()
    location = forms.CharField()


    def clean_name(self):
        return self.cleaned_data['name']

    def clean_description(self):
        return self.cleaned_data['description']

    def clean_location(self):
        return self.cleaned_data['location']

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

class CreateAccountForm(forms.Form):
    username = forms.CharField(error_messages={'required': 'Please enter a valid username'})
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.ChoiceField(
            choices=[('M','Male'),('F','Female'),('SCB','Space Cowboy'), ('SCG', 'Space Cowgirl'), ('SB', 'Space Bear')]
            )
    email = forms.EmailField()
    password = forms.CharField( widget=forms.PasswordInput() )
    confirm_password= forms.CharField( widget=forms.PasswordInput() ) 
    profile_picture = forms.ImageField(label='Upload a profile picture!', required=False)


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

    def clean_profile_picture(self):
        picture_passed = self.cleaned_data['profile_picture']
        return picture_passed

    def clean(self):
        password = self.cleaned_data['password']
        confirmed_password = self.cleaned_data['confirm_password'] 
        firstname = self.cleaned_data['first_name']
        lastname = self.cleaned_data['last_name']
        username = self.cleaned_data['username']

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
        
    def clean_first_name(self):
        data = self.cleaned_data['first_name']
        return data

    def clean_last_name(self):
        data = self.cleaned_data['last_name']
        return data
    
    def clean_email(self):
        data = self.cleaned_data['email']
        return data

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class UpdateProfileExtendedForm(forms.ModelForm):
        
    def clean_gender(self):
        gender = self.cleaned_data['gender']
        return gender
    
    class Meta:
        model = Owner
        fields = ['gender']








