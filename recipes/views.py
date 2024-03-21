from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q 
from django.db import IntegrityError
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm, SearchForm

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

    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)

    if recipe.status == 0 and recipe.author != request.user:
        return render(request, 'recipes/my_recipe_list.html', {'recipe': recipe})

    is_favorite = False
    if request.user.is_authenticated:
        is_favorite = request.user.favorite.filter(slug=recipe.slug).exists()

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
        'is_favorite': is_favorite,
        },
        
    )

def index(request):
    """View function for home page of site."""

    featured_recipes = Recipe.objects.filter(is_featured=True)
    context = {
        'featured_recipes': featured_recipes,
    }
    return render(request, 'recipes/index.html', context=context)


def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user  
            recipe.slug = slugify(recipe.title)
            
            # Check if the slug already exists
            existing_slugs = Recipe.objects.filter(slug__startswith=recipe.slug)
            if existing_slugs.exists():
                recipe.slug = f"{recipe.slug}-{existing_slugs.count() + 1}"
            
            recipe.save()
            
            if recipe.status == 0:
                messages.add_message(request, messages.SUCCESS, 'Draft recipe added successfully!')
            else:
                messages.add_message(request, messages.ERROR, 'Recipe published successfully!')

            return redirect('recipe_detail', slug=recipe.slug)
        else:
            messages.error(request, 'Error adding recipe.')
    else:
        form = RecipeForm()
    
    return render(request, 'recipes/add_recipe.html', {'form': form})


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``post``
        An instance of :model:`recipes.Recipe`.
    ``comment``
        A single comment related to the recipe.
    ``comment_form``
        An instance of :form:`recipe.CommentForm`
    """
    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR,
                                 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    Delete an individual comment.

    **Context**

    ``recipe``
        An instance of :model:`recipes.Recipe`.
    ``comment``
        A single comment related to the recipe.
    """
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


def recipe_edit(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid() and recipe.author == request.user:
            new_recipe = form.save(commit=False)
            new_recipe.slug = slugify(new_recipe.title)
            new_recipe.save()
            messages.add_message(request, messages.SUCCESS, 'Recipe updated!')
            return redirect('recipe_detail', slug=new_recipe.slug)
        else:
            messages.add_message(request, messages.ERROR, 'Error editing recipe!')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_edit.html', {'form': form})


def recipe_delete(request, slug):
    queryset = Recipe.objects.all()
    recipe = get_object_or_404(queryset, slug=slug)
    
    if recipe.author == request.user:
        recipe.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'Error deleting recipe!')

    return HttpResponseRedirect(reverse('recipes_list'))
    
    
def my_recipe_list(request):
    user = request.user
    published_recipes = Recipe.objects.filter(author=user, status=1)
    draft_recipes = Recipe.objects.filter(author=user, status=0)
    context = {
        'published_recipes': published_recipes,
        'draft_recipes': draft_recipes,
    }
    return render(request, 'recipes/my_recipe_list.html', context)


def search_results(request):
    query = request.GET.get('q')

    if not query:
        messages.error(request, "Please enter a search query.")
        return render(request, 'recipes/search_results.html', {'recipes': []})

    if len(query) > 100:
        messages.error(request, "Search query is too long. Maximum length is 100 characters.")
        return render(request, 'recipes/search_results.html', {'recipes': []})

    recipes = Recipe.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    
    return render(request, 'recipes/search_results.html', {'recipes': recipes})



def favorite_recipes(request):
    favorite_recipes = request.user.favorite.all()
    return render(request, 'recipes/favorite_recipes.html', {'favorite_recipes': favorite_recipes})
    

def add_to_favorites(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    if request.user.favorite.filter(slug=slug).exists():
        message = "Recipe already in favorites"
    else:
        request.user.favorite.add(recipe)
        message = "Recipe added to favorites"

    return JsonResponse({'message': message})


def remove_from_favorites(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    
    if request.user.favorite.filter(slug=slug).exists():
        request.user.favorite.remove(recipe)
        message = "Recipe removed from favorites"
    else:
        message = "Recipe is not in favorites"

    return JsonResponse({'message': message})