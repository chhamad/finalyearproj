from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import CustomUserForm

@login_required
def edit_profile(request):
    user = request.user
    custom_user = user.customuser

    if request.method == 'POST':
        form = CustomUserForm(request.POST,request.FILES, instance=user)

        if form.is_valid():
            form.save()
            return redirect('edit_profile')  # Redirect to the profile page after saving
    else:
        form = CustomUserForm(instance=user, initial={
            'user_type': custom_user.user_type,
            'bio': custom_user.bio,
            'specialization': custom_user.specialization,
            'location': custom_user.location,
        })


    return render(request, 'edit_profile.html', {'form': form})
