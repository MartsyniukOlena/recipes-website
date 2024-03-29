# Generated by Django 4.2.11 on 2024-03-12 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-created_on']},
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
