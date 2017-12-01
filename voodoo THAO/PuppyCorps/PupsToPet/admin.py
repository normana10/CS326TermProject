from django.contrib import admin
from .models import Pet, Owner, Event, Breed

# Register your models here.

#admin.site.register(Pet)
#admin.site.register(Owner)
#admin.site.register(Event)
admin.site.register(Breed)


# Define the Pet admin class
class PetAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name', 'age', 'owner', 'service', 'vaccinated', 'gender', 'size')

# Register the Pet admin class with the associated model
admin.site.register(Pet, PetAdmin)

class OwnerAdmin(admin.ModelAdmin):
    list_display = ('ID', '__str__')

admin.site.register(Owner, OwnerAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name', 'host', 'start_time', 'end_time', 'location' )

admin.site.register(Event, EventAdmin)

##class BreedAdmin(admin.ModelAdmin):
##    pass
##
##admin.site.register(Breed, BreedAdmin)


