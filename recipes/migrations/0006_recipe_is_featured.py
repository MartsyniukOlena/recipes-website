# Generated by Django 4.2.11 on 2024-03-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_rename_post_comment_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='is_featured',
            field=models.BooleanField(default=False),
        ),
    ]