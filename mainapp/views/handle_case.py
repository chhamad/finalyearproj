# mainapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms import CaseForm
from ..models import Case, CustomUser

@login_required
def handle_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save(commit=False)
            case.client = request.user.customuser
            case.save()

            lawyer_id = request.GET.get('lawyer_id')
            if lawyer_id:
                lawyer = CustomUser.objects.get(id=lawyer_id)
                case.lawyer = lawyer  # Assign the lawyer if provided
                case.save()

            return redirect('my_lawyer')
    else:
        form = CaseForm()

    return render(request, 'handle_case.html', {'form': form})


