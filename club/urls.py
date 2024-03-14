from . import views
from django.urls import path

urlpatterns = [
    path('', views.club_gourmet, name='club'),
]