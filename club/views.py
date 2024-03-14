from django.shortcuts import render
from .models import Club

# Create your views here.
def club_gourmet(request):
    """
    Renders the Gourmet Club page
    """
    club = Club.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "club/club.html",
        {"club": club},
    )
