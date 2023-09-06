const stars = document.querySelectorAll('.star');
const reviewScoreInput = document.getElementById('review_score');

stars.forEach(star => {
  star.addEventListener('mouseover', function () {
    const value = this.getAttribute('data-value');
    highlightStars(value);
  });

  star.addEventListener('mouseout', function () {
    const value = reviewScoreInput.value;
    highlightStars(value);
  });

  star.addEventListener('click', function () {
    const value = this.getAttribute('data-value');
    reviewScoreInput.value = value;
    highlightStars(value); // Ensure proper highlighting after selection
  });
});

function highlightStars(value) {
  stars.forEach(star => {
    const starValue = star.getAttribute('data-value');
    if (starValue <= value) {
      star.classList.remove('unfilled');
      star.classList.add('filled');
    } else {
      star.classList.remove('filled');
      star.classList.add('unfilled');
    }
  });
}

