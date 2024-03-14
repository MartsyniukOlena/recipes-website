from django.contrib import admin
from .models import Club
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Club)
class ClubAdmin(SummernoteModelAdmin):

    summernote_fields = ('content', 'venue', 'agenda')
