from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ..models import CustomUser

def register_user(request):
    if request.method == 'POST':
        # Get form data from the request
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        # Create a new user object and save it to the database
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password)

        # Check if a CustomUser entry exists for this user
        custom_user, created = CustomUser.objects.get_or_create(user=user)

        # Set the user_type for the CustomUser instance
        custom_user.user_type = user_type
        custom_user.save()

        # Redirect to the home page or a success page after registration
        return redirect('home')  # Assuming the URL name for the home view is 'home'

    # If the request method is GET, render the registration form template
    return render(request, 'register.html')

