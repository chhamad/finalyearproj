// Get the modal
const modal = document.getElementById('myModal');

// Get the button that opens the modal
const openModalButton = document.getElementById('openModalButton'); // Update with your actual button ID

// Get the <span> element that closes the modal
const closeSpan = document.getElementsByClassName('close')[0];

// Get the accept button inside the modal
const acceptButton = document.getElementById('acceptTerms');

// When the user clicks the button, open the modal
openModalButton.addEventListener('click', () => {
    modal.style.display = 'block';
});

// When the user clicks on <span> (x), close the modal
closeSpan.addEventListener('click', () => {
    modal.style.display = 'none';
});

// When the user clicks anywhere outside the modal, close it
window.addEventListener('click', event => {
    if (event.target === modal) {
        modal.style.display = 'none';
    }
});

// When the user clicks the accept button, mark the agreement as accepted
acceptButton.addEventListener('click', () => {
    // You can implement logic here to store the user's acceptance of the agreement
    modal.style.display = 'none';
});
