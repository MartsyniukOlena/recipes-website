# Generated by Django 4.2.11 on 2024-03-14 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('venue', models.TextField()),
                ('agenda', models.TextField()),
                ('datetime', models.DateTimeField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
