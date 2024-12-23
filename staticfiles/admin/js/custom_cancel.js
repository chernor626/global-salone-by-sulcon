document.addEventListener('DOMContentLoaded', function () {
    const cancelButton = document.getElementById('cancel-button');
    if (cancelButton) {
        cancelButton.addEventListener('click', function () {
            alert('Cancel button clicked!');
        });
    }
});


