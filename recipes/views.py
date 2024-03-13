from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipes/recipe_list.html"
    paginate_by = 3


def recipe_detail(request, slug):
    """
    Display an individual :model:`recipes.Recipe`.

    **Context**

    ``post``
        An instance of :model:`recipes.Recipe`.

    **Template:**

    :template:`recipes/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe},
    )
