from django.shortcuts import render


def index(request):
    """Render the home page"""

    return render(request, 'home/index.html')


def terms_and_cond(request):
    return render(request, 'home/terms.html')


def privacy_policy(request):
    return render(request, 'home/privacy.html')