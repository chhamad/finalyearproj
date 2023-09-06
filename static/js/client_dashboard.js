$(document).ready(function() {
    const searchInput = $('#searchInput');
    const lawyerList = $('#lawyerList');

    function filterLawyers(searchQuery) {
        $.ajax({
            url: '/filter_lawyers/',
            data: {
                'search_query': searchQuery,
            },
            dataType: 'json',
            success: function(response) {
                const lawyers = response.lawyers;
                lawyerList.empty();
    
                for (const lawyer of lawyers) {
                    const listItem = $('<li>').addClass('lawyer-item');
    
                    const userProfile = $('<div>').addClass('user-profile');
                    const profileImage = $('<img>').attr('src', lawyer.image_url).attr('alt', 'User Profile').addClass('profile-image');
                    userProfile.append(profileImage);
    
                    const lawyerName = $('<h2>').text(lawyer.username);
                    const specialization = $('<p>').html(`<strong>Specialization:</strong> ${lawyer.specialization}`);
                    const location = $('<p>').html(`<strong>Location:</strong> ${lawyer.location}`);
                    const bio = $('<p>').html(`<strong>Bio:</strong> ${lawyer.bio}`);
                    const avgRating = $('<p>').html(`<strong>Average Rating:</strong> ${lawyer.avg_rating !== null ? lawyer.avg_rating.toFixed(1) : 'Not rated'}`);
    
                    if (lawyer.avg_rating !== null) {
                        for (let i = 1; i <= 5; i++) {
                            const starImage = $('<img>').attr('style', 'width: 20px;');
                            if (i <= lawyer.avg_rating) {
                                starImage.attr('src', '/static/imgs/filled_star.png').attr('alt', 'Filled Star');
                            } else {
                                starImage.attr('src', '/static/imgs/unfilled_star.png').attr('alt', 'Unfilled Star');
                            }
                            avgRating.append(starImage);
                        }
                    } else {
                        avgRating.append('Not rated');
                    }
    
                    const hireLink = $('<a>')
                        .addClass('card-btn')
                        .attr('data-lawyer-id', lawyer.id)  // Pass lawyer ID as a data attribute
                        .text(`Hire ${lawyer.username}`);
                    
                    listItem.append(userProfile, lawyerName, specialization, location, bio, avgRating, hireLink);
                    lawyerList.append(listItem);
                }
    
                // Attach click event to the hire links
                $('.card-btn').on('click', function(event) {
                    event.preventDefault();
                    const lawyerId = $(this).data('lawyer-id');
                    window.location.href = `/create_hiring/${lawyerId}/`;
                });
    
            },
            error: function(error) {
                console.log('Error:', error);
            }
        });
    }
    

    searchInput.on('input', function() {
        const searchQuery = searchInput.val().trim();
        filterLawyers(searchQuery);
    });

    // Initial load of all lawyers
    filterLawyers('');
});



