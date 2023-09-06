from django.shortcuts import render, redirect
from ..forms import ReviewForm
from ..models import Case, CustomUser, Review
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def leave_review(request, lawyer_id):
    lawyer = CustomUser.objects.get(id=lawyer_id)  # Get the lawyer instance

    # Check if the client has already reviewed the lawyer
    existing_review = Review.objects.filter(client=request.user.customuser, lawyer=lawyer).exists()

    if existing_review:
        messages.error(request, 'You already reviewed this lawyer!', extra_tags='error')
        return redirect('search_lawyers')  # Redirect to a page indicating that the review has already been submitted

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.client = request.user.customuser
            review.lawyer = lawyer  # Set the lawyer instance
            review.save()
            return redirect('search_lawyers')  # Redirect to the client dashboard or a success page
    else:
        form = ReviewForm()

    return render(request, 'leave_review.html', {'form': form})

