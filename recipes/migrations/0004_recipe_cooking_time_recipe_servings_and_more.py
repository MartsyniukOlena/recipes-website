# Generated by Django 4.2.11 on 2024-03-12 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_alter_recipe_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveIntegerField(default=0, help_text='Time in minutes', verbose_name='Cooking Time'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='servings',
            field=models.PositiveIntegerField(default=0, help_text='Number of servings', verbose_name='Servings'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created On'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.TextField(verbose_name='Ingredients'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(verbose_name='Instructions'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='updated_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated On'),
        ),
    ]