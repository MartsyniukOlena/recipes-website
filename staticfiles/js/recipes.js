document.addEventListener('DOMContentLoaded', function() {
    const addToFavoritesBtn = document.getElementById('add-to-favorites-btn');
    const removeFromFavoritesBtn = document.getElementById('remove-from-favorites-btn');
    
    function handleAddToFavorites(slug) {
        fetch(`/add-to-favorites/${slug}/`)
            .then(response => response.json())
            .then(data => {

                document.getElementById('alertMessage').innerText = data.message;
                document.getElementById('customAlertModal').style.display = 'block';

                setTimeout(() => {
                    location.reload();
                }, 3000);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    
    function handleRemoveFromFavorites(slug) {
        fetch(`/remove-from-favorites/${slug}/`)
            .then(response => response.json())
            .then(data => {
                document.getElementById('alertMessage').innerText = data.message;
                document.getElementById('customAlertModal').style.display = 'block';
                setTimeout(() => {
                    location.reload();
                }, 3000);
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    

    window.onclick = function(event) {
        let modal = document.getElementById('customAlertModal');
        if (event.target == modal) {
            modal.style.display = 'none';
        }
    }
    

    document.querySelector('.close').addEventListener('click', function() {
        document.getElementById('customAlertModal').style.display = 'none';
    });

    if (addToFavoritesBtn) {
        addToFavoritesBtn.addEventListener('click', function() {
            const slug = addToFavoritesBtn.getAttribute('data-slug');
            handleAddToFavorites(slug);
        });
    }

    if (removeFromFavoritesBtn) {
        removeFromFavoritesBtn.addEventListener('click', function() {
            const slug = removeFromFavoritesBtn.getAttribute('data-slug');
            handleRemoveFromFavorites(slug);
        });
    }
});


const deleteRecipeModal = new bootstrap.Modal(document.getElementById("deleteRecipeModal"));
const deleteRecipeButtons = document.getElementsByClassName("delete-recipe-btn");
const confirmDeleteRecipeButton = document.getElementById("confirmDeleteRecipe");

for (let button of deleteRecipeButtons) {
    button.addEventListener("click", (e) => {
        let slug = e.target.getAttribute("data-recipe-slug");
        confirmDeleteRecipeButton.setAttribute("data-recipe-slug", slug);
        deleteRecipeModal.show();
    });
}

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