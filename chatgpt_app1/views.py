from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return HttpResponse('<b style="color:red">About us</b>')

def contact(request):
    return HttpResponse('<b style="color:red">Contact</b>')

def testimonials(request):
    return HttpResponse('<b style="color:red">Testimonials</b>')

def recent_projects(request):
    return HttpResponse('<b style="color:red">Recent Projects</b>')

def contents(request, first_name, last_name, age):
    age = int(age)
    if age > 0 and age <= 12:
        message = f"Hello {first_name} {last_name},\nThese are contents suitable for kids"
    elif age > 12 and age <= 19:
        message = f"Hello {first_name} {last_name},\nThese are contents suitable for teens"
    elif age > 19 and age <= 58:
        message = f"Hello {first_name} {last_name},\nThese are contents suitable for matured"
    elif age > 58 and age <= 100:
        message = f"Hello {first_name} {last_name},\nThese are contents suitable for senior citizens"
    else:
        message = f"Hello {first_name} {last_name},\nOh Gosh!!! You seem to be an Alien! No contents for you!"
    
    return HttpResponse(f'<b style="color:red">{message}</b>')

