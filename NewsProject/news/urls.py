from django.urls import path
from . import views
urlpatterns=[
    path('',views.search),
    path('latest-news/',views.latNews),
    path('contact-us/',views.contactUs),
    path('<str:slug>/latest-news/',views.allNews),


]
