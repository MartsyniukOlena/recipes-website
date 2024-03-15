from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from .models import Recipe
from .forms import CommentForm, RecipeForm

# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipes/recipe_list.html"
    paginate_by = 3


def recipe_detail(request, slug):
    """
    Display an individual :model:`recipes.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipes.Recipe`.

    **Template:**

    :template:`recipes/recipe_detail.html`
    """

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
    )


    comment_form = CommentForm()

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        },
        
    )

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects - will be replaced with featured recipes
    all_recipes = Recipe.objects.filter(status=1)


    context = {
        'all_recipes': all_recipes,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'recipes/index.html', context=context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  # Set the author to the current logged-in user
            
            # Generate a unique slug based on the recipe title
            recipe.slug = slugify(recipe.title)
            
            # Handle duplicate slugs by appending a number to make it unique
            existing_slugs = Recipe.objects.filter(slug__startswith=recipe.slug)
            if existing_slugs.exists():
                recipe.slug = f"{recipe.slug}-{existing_slugs.count() + 1}"

            recipe.save()
            return redirect('recipes_list')  # Redirect to recipe list page after successful form submission
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})