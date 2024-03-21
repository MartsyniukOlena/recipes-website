from django import forms
from .models import EventForm


class EventForm(forms.ModelForm):
    """
    Form class for users to ask about the event
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = EventForm
        fields = ('name', 'email', 'message')
