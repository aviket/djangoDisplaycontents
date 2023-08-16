from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')



def testimonials(request):
    return render(request, 'testmonials.html')



def recent_projects(request):
    return HttpResponse('<b style="color:red">Recent Projects</b>')


def contents(request, first_name, last_name, age):
    age = int(age)
    greeting = ""
    images = []
    if age > 0 and age <= 12:
        greeting = (
            f"Hello {first_name} {last_name},\nThese are contents suitable for kids"
        )
        images = [
            "for_kid1.jpeg",
            "for_kid2.jpeg",
            "for_kid3.jpeg",
        ]
    elif age > 12 and age <= 19:
        greeting = (
            f"Hello {first_name} {last_name},\nThese are contents suitable for teens"
        )
        images = [
            "for_teen1.jpeg",
            "for_teen2.jpeg",
            "for_teen4.jpeg",
            "for_teen4.jpeg",
        ]
    elif age > 19 and age <= 58:
        greeting = (
            f"Hello {first_name} {last_name},\nThese are contents suitable for matured"
        )
        images = [
            "for_mat1.jpeg",
            "for_mat2.jpeg",
            "for_mat3.jpeg",
            "for_mat4.jpeg",
        ]
    elif age > 58 and age <= 100:
        greeting = f"Hello {first_name} {last_name},\nThese are contents suitable for senior citizens"
        images = [
            "for_sinior1.jpeg",
            "for_sinior2.jpeg",
            "for_sinior3.jpeg",
        
        ]
    else:
        greeting = f"Hello {first_name} {last_name},\nOh Gosh!!! You seem to be an Alien! No contents for you!"

    return render(request, "contents.html", {"greeting": greeting, "images": images})
