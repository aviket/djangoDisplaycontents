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
