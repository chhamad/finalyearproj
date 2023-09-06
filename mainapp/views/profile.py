from django.shortcuts import render, get_object_or_404
from ..models import CustomUser
from django.contrib.auth.decorators import login_required



@login_required
def my_profile(request):
    user = request.user

    context = {
        'user': user
    }
    return render(request, 'my_profile.html', context)

def view_profile(request, lawyer_id):
    lawyer = get_object_or_404(CustomUser, id=lawyer_id, user_type='Lawyer')

    context = {
        'lawyer': lawyer
    }
    return render(request, 'lawyer_profile.html', context)



