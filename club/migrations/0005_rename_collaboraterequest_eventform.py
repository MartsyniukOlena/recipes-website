# Generated by Django 4.2.11 on 2024-03-19 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_collaboraterequest_club_profile_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CollaborateRequest',
            new_name='EventForm',
        ),
    ]
