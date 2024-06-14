document.addEventListener('DOMContentLoaded', function () {
    const deleteRecipeModal = new bootstrap.Modal(document.getElementById("deleteRecipeModal"));
    const deleteRecipeButtons = document.getElementsByClassName("delete-recipe-btn");
    const deleteRecipeForm = document.getElementById("delete-recipe-form");

    for (let button of deleteRecipeButtons) {
        button.addEventListener("click", (e) => {
            let slug = e.target.getAttribute("data-recipe-slug");
            deleteRecipeForm.action = `/${slug}/delete_recipe/`; 
            deleteRecipeModal.show();
        });
    }
});