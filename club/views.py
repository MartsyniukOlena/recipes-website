from django.shortcuts import render
from django.contrib import messages
from .models import Club
from .forms import EventForm

# Create your views here.


def club_gourmet(request):
    """
    Renders the most recent information on the club
    and allows user attendance requests.

    Displays an individual instance of :model:`club.Club`.

    **Context**
    ``club``
        The most recent instance of :model:`club.Club`.
        ``event_form``
            An instance of :form:`club.EventForm`.
    **Template**
    :template:`club/club.html`
    """

    if request.method == "POST":
        event_form = EventForm(data=request.POST)
        if event_form.is_valid():
            event_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your message was received! I endeavour to respond within 2 working days.'
            )
    club = Club.objects.all().order_by('-updated_on').first()
    event_form = EventForm()

    return render(
        request,
        "club/club.html",
        {"club": club, "event_form": event_form},
    )
