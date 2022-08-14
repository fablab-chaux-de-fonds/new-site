from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(OpeningSlot)
class OpeningSlotAdmin(admin.ModelAdmin):
    list_display = ['opening', 'start', 'end', 'user']

@admin.register(EventSlot)
class EventSlotAdmin(admin.ModelAdmin):
    list_display = ['event', 'start', 'end', 'user', 'is_active', 'has_registration']