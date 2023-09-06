# mainapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def login_user(request):
    if request.method == 'POST':
        # Get form data from the request
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user credentials
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to the home page or a success page after successful login
            return redirect('home')  # Assuming the URL name for the home view is 'home'
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error': 'Invalid login credentials'})

    # If the request method is GET, render the login form template
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('home')  # Redirect to the home page after logout