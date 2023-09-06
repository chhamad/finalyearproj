from django.shortcuts import render, redirect
from ..forms import ReviewForm
from ..models import Case, CustomUser,Hiring
from django.contrib.auth.decorators import login_required
from ..forms import LawyerSearchForm
from django.db.models import Avg
from django.contrib import messages





def create_hiring(request, lawyer_id):
    lawyer = CustomUser.objects.get(id=lawyer_id)
    client = request.user.customuser
    
    # Check if the hiring relationship already exists
    if Hiring.objects.filter(client=client, hired_lawyers=lawyer).exists():
        messages.warning(request, "You already hired this lawyer!")
    else:
        # Create a new Hiring instance
        hiring = Hiring.objects.create(client=client)
        hiring.hired_lawyers.add(lawyer)
    
    return redirect('my_lawyer')




def my_lawyer(request):
    client = request.user.customuser
    hired_lawyers = CustomUser.objects.filter(hired_lawyers__client=client)

    lawyers_with_case = Case.objects.filter(client=client).values_list('lawyer', flat=True)

    for lawyer in hired_lawyers:
        lawyer.has_case = lawyer.id in lawyers_with_case
    
    context = {
        'client': client,
        'hired_lawyers': hired_lawyers,
    }
    return render(request, 'my_lawyer.html', context)





def delete_hiring(request, lawyer_id):
    client = request.user.customuser
    lawyer = CustomUser.objects.get(id=lawyer_id)
    
    try:
        hiring = Hiring.objects.get(client=client, hired_lawyers=lawyer)
        hiring.delete()

        # Delete cases related to the client and lawyer
        Case.objects.filter(client=client, lawyer=lawyer).delete()

    except Hiring.DoesNotExist:
        pass
    
    return redirect('my_lawyer')

    


def search_lawyers(request):
    form = LawyerSearchForm()

    if request.method == 'GET':
        form = LawyerSearchForm(request.GET)

        specialization = request.GET.get('specialization', None)
        location = request.GET.get('location', None)
        
        if specialization:
            lawyers = CustomUser.objects.filter(user_type='Lawyer', specialization__icontains=specialization)
        else:
            lawyers = CustomUser.objects.filter(user_type='Lawyer')
        
        if location:
            lawyers = lawyers.filter(location__icontains=location)

        lawyers = lawyers.annotate(avg_rating=Avg('lawyer_reviews__review_score'))

        context = {
            'form': form,
            'lawyers': lawyers
        }
        return render(request, 'search_lawyers.html', context)

    context = {
        'form': form
    }
    return render(request, 'search_lawyers.html', context)