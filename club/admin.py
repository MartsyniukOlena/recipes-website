from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Club, EventForm


# Register your models here.

@admin.register(Club)
class ClubAdmin(SummernoteModelAdmin):
    """
    Adds rich-text editing of content in admin
    """
    summernote_fields = ('content',)


@admin.register(EventForm)
class EventFormAdmin(admin.ModelAdmin):
    """
    Lists message and read fields for display in admin
    """
    list_display = ('message', 'read',)
