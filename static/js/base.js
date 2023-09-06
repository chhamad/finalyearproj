// Add this code to your JavaScript file (e.g., client_dashboard.js)
$(document).ready(function() {
    // Automatically remove the message element after 5 seconds
    $('.alert').delay(5000).fadeOut(500, function() {
        $(this).remove();
    });
});
