from django.test import TestCase
from django.urls import reverse
from .models import Club
from .forms import EventForm

# Create your tests here.


class TestClubView(TestCase):

    def setUp(self):
        """Creates club content"""
        self.club_content = Club(
            title="Welcome", content="This is about club.")
        self.club_content.save()

    def test_render_club_page_with_event_form(self):
        """Verifies get request for club containing an event form"""
        response = self.client.get(reverse('club'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Club', response.content)
        self.assertIsInstance(
            response.context['event_form'], EventForm)

    def test_successful_event_form_submission(self):
        """Test for a user to fill in the form"""
        post_data = {
            'name': 'test name',
            'email': 'test@email.com',
            'message': 'test message'
        }
        response = self.client.post(reverse('club'), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Your message was received! I endeavourto respond within 2 working days.',response.content)
