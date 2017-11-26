import uuid
from django.db import models
from django.urls import reverse


#We will need code that lets the user upload pictures of themselves/their pets

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

class Pet(models.Model):
    """
    Defines Pet model
    """
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Pet's unique id")
    name = models.CharField(max_length=100, null=True, help_text="Enter pet's name")
    age = models.CharField(max_length=2, null=True, help_text="How old is your pet? Enter a number. (ex: '2', '10', or '15')")
  #  karma = models.FloatField(null=True, help_text="Pet's average rating")
    owner = models.ForeignKey('Owner', on_delete=models.SET_NULL, null=True, help_text="Pet's owner")
    service = models.BooleanField(default=False, help_text="Is this a service animal?")
    vaccinated = models.BooleanField(default=False, help_text="Is this pet vaccinated?")
    disposition = models.CharField(max_length=200, null=True, help_text="Write some notes about your pet's disposition/personality.")
    additional_notes= models.TextField(max_length=1000, null=True, help_text="What else should we know about your pet? Write them down here!")

    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'))
    gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES, blank=True, help_text="Pet's gender")

    SIZE_CHOICES = (('S', 'small'), ('M', 'medium'), ('L', 'large'))
    size = models.CharField(max_length=1, choices=SIZE_CHOICES, blank=True, help_text="Pet's size")


    # Breed class has already been defined so we can specify the object below.
    breed = models.ManyToManyField(Breed, help_text="Your pet might be pure-bred or mixed! Select the breed(s) for this pet.")     

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('pet-detail', args=[str(self.ID)])
    
    def __str__(self):
        """
        String for representing the Pet object (in Admin site etc.)
        """
        return self.name

    def display_breed(self):
        """
        Creates a string for the Breed. This is required to display breed in Admin.
        """
        return ', '.join([ breed.name for breed in self.breed.all()[:3] ])
    display_breed.short_description = 'Breed'

class Owner(models.Model):
    """
    Defines Owner model
    """
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Owner's unique id")
 first_name = models.CharField(max_length=100,null=True,help_text="Owner's first name")
 last_name = models.CharField(max_length=100,null=True,help_text="Owner's last name")
 username = models.CharField(max_length=100,null=True,help_text="Owner's username")
 email = models.EmailField(null=True, help_text="email address")
# pet_owner_status = models.BooleanField(default=False, help_text="Are you a dog owner?")
user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = (('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, default='M', choices=GENDER_CHOICES, blank=True, help_text="Owner's gender")
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular owner instance.
        """
        return reverse('owner-detail', args=[str(self.ID)])
        
    # Methods
    def __str__(self):
        """
        String for representing the Owner object (in Admin site etc.)
        """
        return '%s, %s, %s' % (self.username, self.last_name, self.first_name)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Owner.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.owner.save()

class Event(models.Model):
    """
    Defines Event model
    """
    name = models.CharField(max_length=75,null=True,help_text="Event name")
    ID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for each event")
    host = models.ForeignKey('Owner',on_delete=models.SET_NULL,null=True,help_text="Host of event")
    pet = models.ManyToManyField(Pet,help_text="Pets attending event")
 #   pet = models.ForeignKey('Pet',on_delete=models.SET_NULL,null=True,help_text="Owner's pet")
    start_time = models.DateTimeField(max_length=10,null=True,help_text="Enter time that event starts")
    end_time = models.DateTimeField(max_length=10,null=True,help_text="Enter time that event ends")
    description = models.CharField(max_length=300, null=True, help_text="Enter event description here!")
    location = models.CharField(max_length=100,null=True,help_text="Enter event location") #special data type?

    # Methods
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a particular owner instance.
        """
        return reverse('event-detail', args=[str(self.ID)])

    class Meta:
        ordering = ["start_time", "name", "host", "ID"]

##class Location(models.Model):
##    """
##    Defines Location model
##    """
##    location = models.CharField(max_length=100), gps = Coo
# reviews
# locations
# sharing/store
