from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from django.http import HttpResponseRedirect, JsonResponse
from django.db.models import Q
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm, SearchForm


# Create your views here.


class RecipeList(generic.ListView):
    """
    Returns all published recipes in :model:`recipes.Recipe`
    and displays them in a page of three posts.
    **Context**

    ``queryset``
        All published instances of :model:`recipes.Recipe`
    ``paginate_by``
        Number of recipes per page.
    **Template:**

    :template:`recipes/recipe_list.html`
    """
    queryset = Recipe.objects.filter(status=1)
    template_name = "recipes/recipe_list.html"
    paginate_by = 3


def recipe_detail(request, slug):
    """
    Display an individual :model:`recipes.Recipe`.

    **Context**

    ``recipe``
        An instance of :model:`recipes.Recipe`.
    ``comments``
        All approved comments related to the post.
    ``comment_count``
        A count of approved comments related to the post.
    ``comment_form``
        An instance of :form:`recipes.CommentForm`
    ``is_favorite``
        Indicates whether the current recipe is marked
        as a favorite by the logged-in user.

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
                'Comment submitted and awaiting approval')
    comment_form = CommentForm()

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        'is_favorite': is_favorite, },
    )


def index(request):
    """
    View function for the home page.
    Retrieves featured recipes to display on the home page.

    **Context**

    ``featured_recipes``
        An instance of :model:`recipes.Recipe`.

    **Template:**

    :template:`recipes/index.html`
    """

    featured_recipes = Recipe.objects.filter(is_featured=True)
    context = {
        'featured_recipes': featured_recipes,
    }
    return render(request, 'recipes/index.html', context=context)


def add_recipe(request):
    """
    View function for adding a new recipe.
    Automatically generates a slug for the recipe title
    and handles potential slug conflicts by appending a count.

    **Context**

    ``form``
        An instance of :form:`recipes.RecipeForm`

    **Template:**

    :template:`recipes/add_recipe.html`
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only authenticated users can add recipes.')
        return redirect(reverse('account_login'))

    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.slug = slugify(recipe.title)
            try:
                recipe.save()
                if recipe.status == 0:
                    messages.add_message(request, messages.SUCCESS, 'Draft recipe added successfully!')
                else:
                    messages.add_message(request, messages.SUCCESS, 'Recipe published successfully!')
                return redirect('recipe_detail', slug=recipe.slug)
            except IntegrityError:
                messages.add_message(request, messages.ERROR, 'A recipe with the same title already exists. Please choose a different title.')
        else:
            messages.add_message(request, messages.ERROR, 'Error adding recipe.')
    else:
        form = RecipeForm()
    return render(request, 'recipes/add_recipe.html', {'form': form})


def comment_edit(request, slug, comment_id):
    """
    Display an individual comment for edit.

    **Context**

    ``recipe``
        An instance of :model:`recipes.Recipe`.
    ``comment``
        A single comment related to the recipe.
    ``comment_form``
        An instance of :form:`recipes.CommentForm`
    """

    if not request.user.is_authenticated:
        messages.error(request, 'Please, sign in to edit your comments.')
        return redirect(reverse('account_login'))

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)
    comment_form = CommentForm(data=request.POST, instance=comment)

    if comment.author != request.user:
        messages.add_message(request, messages.ERROR, 'You can only edit your own comments!')
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid():
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

    if not request.user.is_authenticated:
        messages.error(request, 'Please, sign in to delete your comments.')
        return redirect(reverse('account_login'))

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
    """
    View function for editing an existing recipe.
    Retrieves the recipe with the given slug from the database.
    **Context**
    ``form``
        An instance of :form:`recipes.RecipeForm`
    **Template:**
    :template:`recipes/edit_recipe.html`
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    if not request.user.is_authenticated:
        messages.error(request, 'Please, sign in to edit your recipes.')
        return redirect(reverse('account_login'))

    if recipe.author != request.user:
        messages.error(request, 'Sorry, only the author can edit this recipe.')
        return redirect(reverse('recipe_detail', args=[slug]))

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            updated_recipe = form.save(commit=False)
            updated_recipe.slug = slugify(updated_recipe.title)
            updated_recipe.save()
            messages.success(request, 'Successfully updated recipe!')
            return redirect(reverse('recipe_detail', args=[updated_recipe.slug]))
        else:
            messages.error(request, 'Failed to update recipe. Please ensure the form is valid.')
    else:
        form = RecipeForm(instance=recipe)
        messages.info(request, f'You are editing {recipe.title}')

    template = 'recipes/recipe_edit.html'
    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, template, context)


def recipe_delete(request, slug):
    """
    View function for deleting an existing recipe.

    Retrieves the recipe with the given slug from the database.
    Deletes the recipe if the current user is the author.

     **Context**

    ``recipe``
        An instance of :model:`recipes.Recipe`.
    """

    if not request.user.is_authenticated:
        messages.error(request, 'Please, sign in to delete your recipes.')
        return redirect(reverse('account_login'))

    recipe = get_object_or_404(Recipe, slug=slug)

    if recipe.author != request.user:
        messages.error(request, 'Sorry, only the author can delete this recipe.')
        return redirect(reverse('recipe_detail', args=[slug]))

    if request.method == 'POST':
        recipe.delete()
        messages.success(request, 'Recipe deleted!')
        return redirect(reverse('recipes_list'))
    else:
        return redirect(reverse('recipe_detail', args=[slug]))


def my_recipe_list(request):
    """
    View function for displaying a list of recipes authored by the current user.

    Retrieves both published and draft recipes authored by the current user.
    Separates published recipes from draft recipes.

    **Context**

    ``published_recipes``
        An instance of :model:`recipes.Recipe`
    ``draft_recipes``
        An instance of :model:`recipes.Recipe`

    **Template**

    recipes/my_recipe_list.html
    """

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only authenticated users can access My Recipes page.')
        return redirect(reverse('account_login'))

    user = request.user
    published_recipes = Recipe.objects.filter(author=user, status=1)
    draft_recipes = Recipe.objects.filter(author=user, status=0)
    context = {
        'published_recipes': published_recipes,
        'draft_recipes': draft_recipes,
    }
    return render(request, 'recipes/my_recipe_list.html', context)


def search_results(request):
    """
    View function for displaying search results based on user query.

    Retrieves the search query entered by the user from the request.
    Validates the search query and displays appropriate error messages if invalid.
    Performs a search on recipe titles and content containing the query.
    Returns a list of recipes matching the search query to be displayed.

    **Context**
    ''recipes''
        An instance of :model:`recipes.Recipe`

    **Template**
    recipes/search_results.html
    """
    query = request.GET.get('q')

    if not query:
        messages.add_message(request, messages.ERROR, "Please enter a search query.")
        return render(request, 'recipes/search_results.html', {'recipes': []})

    if len(query) > 100:
        messages.add_message(request, messages.ERROR, "Search query is too long. Maximum length is 100 characters.")
        return render(request, 'recipes/search_results.html', {'recipes': []})

    recipes = Recipe.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
    return render(request, 'recipes/search_results.html', {'recipes': recipes})


def favorite_recipes(request):
    """
    View function for displaying a list of favorite recipes for the current user.
    Retrieves all recipes marked as favorites by the current user.

    **ontext**
        ''favorite_recipes''
            A queryset containing all recipes marked as favorites by the current user.

    **Template**
    recipes/favorite_recipes.html
    """
    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only authenticated users can access Favorities page.')
        return redirect(reverse('account_login'))

    favorite_recipes = request.user.favorite.all()
    return render(request, 'recipes/favorite_recipes.html', {'favorite_recipes': favorite_recipes})


def add_to_favorites(request, slug):
    """
    View function for adding a recipe to the user's favorites.
    Adds the recipe to the favorites of the current user if it's not already there.
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only authenticated users can add recipes to Favorities.')
        return redirect(reverse('account_login'))

    if request.user.favorite.filter(slug=slug).exists():
        messages.info(request, "Recipe already in Favorites")
    else:
        request.user.favorite.add(recipe)
        messages.success(request, "Recipe added to Favorites")
    return redirect(reverse('recipe_detail', args=[slug]))


def remove_from_favorites(request, slug):
    """
    View function for removing a recipe from the user's favorites.
    """
    recipe = get_object_or_404(Recipe, slug=slug)

    if not request.user.is_authenticated:
        messages.error(request, 'Sorry, only authenticated users can remove recipes from Favorities.')
        return redirect(reverse('account_login'))

    if request.user.favorite.filter(slug=slug).exists():
        request.user.favorite.remove(recipe)
        messages.success(request, "Recipe removed from Favorites")
    else:
        messages.info(request, "Recipe is not in Favorites")
    return redirect(reverse('recipe_detail', args=[slug]))
