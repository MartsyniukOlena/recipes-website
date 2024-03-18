document.addEventListener('DOMContentLoaded', function() {
    const addToFavoritesBtn = document.getElementById('add-to-favorites-btn');
    const removeFromFavoritesBtn = document.getElementById('remove-from-favorites-btn');
    
    function handleAddToFavorites(slug) {
        fetch(`/add-to-favorites/${slug}/`)
            .then(response => response.json())
            .then(data => {
                alert(data.message); // You can handle success message in a better way
                location.reload(); // Reload the page
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }
    
    function handleRemoveFromFavorites(slug) {
        fetch(`/remove-from-favorites/${slug}/`)
            .then(response => response.json())
            .then(data => {
                alert(data.message); // You can handle success message in a better way
                location.reload(); // Reload the page
            })
            .catch(error => {
                console.error('Error:', error);
            });
    }

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