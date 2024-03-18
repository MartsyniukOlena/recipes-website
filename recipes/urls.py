from . import views
from django.urls import path
from .views import add_to_favorites

urlpatterns = [
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('add-to-favorites/<slug:slug>/', views.add_to_favorites, name='add_to_favorites'),
    path('favorite-recipes/', views.favorite_recipes, name='favorite_recipes'),
    path('remove-from-favorites/<slug:slug>/', views.remove_from_favorites, name='remove_from_favorites'),
    path('recipes/', views.RecipeList.as_view(), name='recipes_list'),
    path('my_recipes/', views.my_recipe_list, name='my_recipe_list'),
    path('search/', views.search_results, name='search_results'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/edit_recipe/',
         views.recipe_edit, name='recipe_edit'),
    path('<slug:slug>/delete_recipe/',
         views.recipe_delete, name='recipe_delete'),
    path('', views.index, name='index'),
    
]
