from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('recent_projects', views.recent_projects, name='recent_projects'),
   path('contents/<str:first_name>/<str:last_name>/<int:age>/', views.contents, name='contents'),
]
