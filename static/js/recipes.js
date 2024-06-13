document.addEventListener('DOMContentLoaded', function () {
    let deleteButtons = document.querySelectorAll('.delete-recipe-btn');
    let deleteForm = document.getElementById('delete-recipe-form');
    let deleteModal = new bootstrap.Modal(document.getElementById('deleteRecipeModal'));

    for (let button of deleteButtons) {
        button.addEventListener("click", (e) => {
            let recipeSlug = e.target.getAttribute("data-recipe-slug");
            deleteForm.action = `/${recipeSlug}/delete_recipe/`;
        });
    }
});