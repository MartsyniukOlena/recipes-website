// Function to hide the alert after a certain time
setTimeout(function() {
    let alertContainer = document.getElementById('alert-container');
    if (alertContainer) {
        alertContainer.remove();
    }
}, 3000);