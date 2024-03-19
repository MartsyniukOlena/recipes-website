from django.contrib import admin
from .models import Club, EventForm
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Club)
class ClubAdmin(SummernoteModelAdmin):

    summernote_fields = ('content',)


@admin.register(EventForm)
class EventFormAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)
