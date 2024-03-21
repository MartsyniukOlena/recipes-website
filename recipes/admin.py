from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    """
    Lists fields for display in admin, fileds for search,
    field filters, fields to prepopulate and rich-text editor.
    """

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}


# Register your models here.

admin.site.register(Comment)