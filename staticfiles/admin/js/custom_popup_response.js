document.addEventListener('DOMContentLoaded', function () {
    const popupButton = document.getElementById('popup-button');
    if (popupButton) {
        popupButton.addEventListener('click', function () {
            alert('Popup button clicked!');
        });
    }
});
