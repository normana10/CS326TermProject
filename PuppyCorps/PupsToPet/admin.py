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
    list_display = ('ID', 'first_name', 'last_name', 'username', 'email', 'gender')

admin.site.register(Owner, OwnerAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('ID', 'name', 'host', 'start_time', 'end_time', 'location' )

admin.site.register(Event, EventAdmin)

##class BreedAdmin(admin.ModelAdmin):
##    pass
##
##admin.site.register(Breed, BreedAdmin)


'''
class PetInline(admin.TabularInline):
    model = Pet
    extra = 0
    
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('username','id','firstName', 'lastName')
    inlines = [PetInline]
    
@admin.register(Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ('name','id')
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id','host','startTime','endTime')
    list_filter=('startTime','endTime')
'''