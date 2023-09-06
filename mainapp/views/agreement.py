from django.shortcuts import render

def terms_of_service(request):
    return render(request, 'terms_of_service.html')

def user_agreement(request):
    return render(request, 'user_agreement.html')
