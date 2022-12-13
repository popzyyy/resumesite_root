from django.http import request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from bruh.forms import ContactForm
from bruh.models import *
from django.contrib.gis.geoip2 import GeoIP2
import turtle
from resumesite import settings


def refresh(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def home(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    g = GeoIP2()
    # change to ip not 67.3.184.28
    data = g.city('67.3.184.28')
    city = data['city']
    state = data['region']
    country = data['country_name']
    lat = data['latitude']
    long = data['longitude']
    zipcode = data['postal_code']
    exists = Visitor.objects.filter(ipaddress=ip).exists()
    if not exists:
        bruh = Visitor(ipaddress=ip, city=city, state=state, country=country, latitude=lat, longitude=long,
                       zipcode=zipcode)
        bruh.save()

    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def resume(request):
    return render(request, 'resume.html')


def experience(request):
    return render(request, 'experience.html')


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            try:
                subject = "Website Inquiry"
                body = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'message': form.cleaned_data['message'],
                }
                message = "\n".join(body.values())

                send_mail(subject=subject, message=message, from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=("spress61@live.com"), fail_silently=True)
            except:
                pass


        return render(request, 'contact_success.html')




    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})










def portfolio(request):



    return render(request, 'portfolio.html')



def games(request):
    return render(request, 'games.html')


def interests(request):
    return render(request, 'interests.html')

def windows(request):
    return render(request, 'windows.html')
