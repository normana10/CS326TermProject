from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Pet(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for each pet")
    name=models.CharField(max_length=100,null=True,help_text="pet name")
    owner=models.ForeignKey('Owner',on_delete=models.SET_NULL,null=True,help_text="owner of pet")
    #karma=models.FloatField(null=True,help_text="average rating of pet")
    
    SIZE=(('S','small'),('M','medium'),('L','large'))
    gender=models.CharField(max_length=1, default='M', choices=SIZE, blank=True, help_text="Pet's size")
    
    GENDER=(('M','Male'),('F','Female'))
    gender=models.CharField(max_length=1, default='M', choices=GENDER, blank=True, help_text="Pet's gender")
    
    service=models.BooleanField(default=False,help_text="is this a service animal")
    vacinated=models.BooleanField(default=False,help_text="is this pet vacinated")
    disposition=models.CharField(max_length=200,null=True,help_text="notes about pet's disposition")
    additional_notes=models.TextField(max_length=1000,null=True,help_text="summary and additional notes about pet")
    
    breed = models.ManyToManyField('Breed', help_text="Your pet might be pure-bred or mixed! Select the breed(s) for this pet.")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
    class Meta:
        ordering = ["name","id"]
        
class Owner(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for each owner")
    firstName=models.CharField(max_length=100,null=True,help_text="owner's first name")
    lastName=models.CharField(max_length=100,null=True,help_text="owner's last name")
    username=models.CharField(max_length=100,null=True,help_text="owner's username")
    email=models.EmailField(null=True,help_text="owner's email adress")
    
    GENDER=(('M','Male'),('F','Female'))
    gender=models.CharField(max_length=1, choices=GENDER, blank=True, help_text="Owner's gender")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.username
        #return "{0} {1}".format(self.firstName,self.lastName)
        
    class Meta:
        ordering = ["username","id"]
        #ordering = ["lastName","firstName","id"]
        
class Event(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for each event")
    host=models.ForeignKey('Owner',on_delete=models.SET_NULL,null=True,help_text="host of event")
    pet=models.ManyToManyField('Pet',help_text="pets attending event")
    
    startTime=models.DateTimeField(max_length=10,null=True,help_text="time that event starts")
    endTime=models.DateTimeField(max_length=10,null=True,help_text="time that event ends")
    loc=models.CharField(max_length=100,null=True,help_text="location event takes place") #special data type?
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return str(id)
        
    def pets(self):
        return ', '.join([p.name for p in self.pet.all()])
    
        
    class Meta:
        ordering = ["startTime","id"]
        
class Breed(models.Model):
    """
    Defines Breed model (e.g. German Sheperd, Golden Retriever, Poodle)
    """
    breed = models.CharField(max_length=200, help_text="Enter a dog breed (e.g. German Sheperd, Golden Retriever, Poodle)")

    def __str__(self):
        """
        String for representing the Breed object (in Admin site etc.)
        """
        return self.breed
        
# reviews
# locations
# sharing/store