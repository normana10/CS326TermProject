from django.contrib import admin
from .models import Pet, Owner, Event

# Register your models here.

#admin.site.register(Pet)
#admin.site.register(Owner)
#admin.site.register(Event)

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