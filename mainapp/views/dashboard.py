# mainapp/views.py

from django.shortcuts import render, redirect
from ..models import CustomUser, Case, Review
from django.db.models import Avg
from django.http import JsonResponse
from ..forms import UpdateCaseStatusForm


def client_dashboard(request):
    client = request.user.customuser
    cases = Case.objects.filter(client=client)
    reviews = Review.objects.filter(client=client)
    lawyers = CustomUser.objects.filter(user_type='Lawyer')  # Get all lawyers
    lawyers = lawyers.annotate(avg_rating=Avg('lawyer_reviews__review_score'))
    context = {
        'client': client,
        'cases': cases,
        'reviews': reviews,
        'lawyers': lawyers,
    }

    return render(request, 'client_dashboard.html', context)



def filter_lawyers(request):
    search_query = request.GET.get('search_query', '').strip()

    if search_query:
        lawyers = CustomUser.objects.filter(
            user_type='Lawyer',
            user__username__icontains=search_query,
        ).annotate(avg_rating=Avg('lawyer_reviews__review_score'))
    else:
        lawyers = CustomUser.objects.filter(user_type='Lawyer').annotate(avg_rating=Avg('lawyer_reviews__review_score'))

    lawyers_data = []
    for lawyer in lawyers:
        # Build a dictionary for each lawyer
        lawyer_data = {
            'id': lawyer.id,
            'username': lawyer.user.username,
            'specialization': lawyer.specialization,
            'location': lawyer.location,
            'bio': lawyer.bio,
            'avg_rating': lawyer.avg_rating,
            'image_url':lawyer.image.url,
        }
        lawyers_data.append(lawyer_data)

    return JsonResponse({'lawyers': lawyers_data})


def cases(request):
    client = request.user.customuser
    cases = Case.objects.filter(client=client)
    context = {
        'client': client,
        'cases': cases,
    }

    return render(request, 'cases.html', context)




def lawyer_cases(request):
    lawyer = request.user.customuser
    cases = Case.objects.filter(lawyer=lawyer)
    
    if request.method == 'POST':
        form = UpdateCaseStatusForm(request.POST)
        if form.is_valid():
            new_status = form.cleaned_data['new_status']
            case_id = request.POST.get('case_id')  # Get the case ID from the hidden input in the form
            case = Case.objects.get(case_id=case_id)
            case.status = new_status
            case.save()
            return redirect('lawyer_cases')
    else:
        form = UpdateCaseStatusForm()

    context = {
        'lawyer': lawyer,
        'cases': cases,
        'form': form,
    }

    return render(request, 'lawyer_cases.html', context)


