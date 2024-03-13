from . import views
from django.urls import path

urlpatterns = [
    path('recipes/', views.RecipeList.as_view(), name='recipes_list'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('', views.index, name='index'),
    
]
