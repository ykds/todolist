from django.contrib import admin

from .models import Event
# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'has_done', 'created_time', 'modified_time']

admin.site.register(Event, EventAdmin)