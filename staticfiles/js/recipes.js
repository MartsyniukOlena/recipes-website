document.addEventListener('DOMContentLoaded', function() {
    /**
    * Function to handle adding a recipe to favorites.
    */
    const addToFavoritesBtn = document.getElementById('add-to-favorites-btn');
    const removeFromFavoritesBtn = document.getElementById('remove-from-favorites-btn');
    
    function handleAddToFavorites(slug) {
        fetch(`/add-to-favorites/${slug}/`)
            .then(response => response.json())
            .then(data => {

                document.getElementById('alertMessage').innerText = data.message;
                document.getElementById('customAlertModal').style.display = 'inline';
                document.getElementById('customAlertModal').style.width = '35%';
                document.getElementById('customAlertModal').style.left = '30%';

                setTimeout(() => {
                    location.reload();
                }, 3000);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    
    /**
    * Function to handle removing a recipe from favorites.
    */
    function handleRemoveFromFavorites(slug) {
        fetch(`/remove-from-favorites/${slug}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('alertMessage').innerText = data.message;
                document.getElementById('customAlertModal').style.display = 'inline';
                document.getElementById('customAlertModal').style.width = '35%';
                document.getElementById('customAlertModal').style.left = '30%';

                setTimeout(() => {
                    location.reload();
                }, 3000);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    
    // Close the modal if clicked outside
    window.onclick = function(event) {
        let modal = document.getElementById('customAlertModal');
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
    
    // Close the modal when close button is clicked
    document.querySelector('.close').addEventListener('click', function() {
        document.getElementById('customAlertModal').style.display = 'none';
    });

    // Event listener for adding recipe to favorites
    if (addToFavoritesBtn) {
        addToFavoritesBtn.addEventListener('click', function() {
            const slug = addToFavoritesBtn.getAttribute('data-slug');
            handleAddToFavorites(slug);
        });
    }
    
    // Event listener for removing recipe from favorites
    if (removeFromFavoritesBtn) {
        removeFromFavoritesBtn.addEventListener('click', function() {
            const slug = removeFromFavoritesBtn.getAttribute('data-slug');
            handleRemoveFromFavorites(slug);
        });
    }
});

// Modal for deleting a recipe
const deleteRecipeModal = new bootstrap.Modal(document.getElementById("deleteRecipeModal"));
const deleteRecipeButtons = document.getElementsByClassName("delete-recipe-btn");
const confirmDeleteRecipeButton = document.getElementById("confirmDeleteRecipe");

// Event listeners for showing delete confirmation modal
for (let button of deleteRecipeButtons) {
    button.addEventListener("click", (e) => {
        let slug = e.target.getAttribute("data-recipe-slug");
        confirmDeleteRecipeButton.setAttribute("data-recipe-slug", slug);
        deleteRecipeModal.show();
    });
}
// Event listener for confirming recipe deletion
confirmDeleteRecipeButton.addEventListener("click", (e) => {
    let slug = e.target.getAttribute("data-recipe-slug");
    window.location.href = `/${slug}/delete_recipe/`;
});

setTimeout(function() {
        let alertContainer = document.getElementById('alert-container');
        if (alertContainer) {
            alertContainer.remove();
        }
    }, 3000);