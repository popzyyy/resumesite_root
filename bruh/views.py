from django.http import request, HttpResponseRedirect
from django.shortcuts import render


def refresh(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def home(request):
    refresh(request)
    return render(request, 'home.html')


def about(request):

    return render(request, 'about.html')


def resume(request):

    return render(request, 'resume.html')


def experience(request):

    return render(request, 'experience.html')


def contact(request):

    return render(request, 'contact.html')