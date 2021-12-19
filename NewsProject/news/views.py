from django.shortcuts import render
from django.urls import reverse
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect
from .models import Contact
import requests
import json
import inspect
from django.contrib import messages


apiKey="Enter Your API here" # In String Format


def home(request):
    res=render(request,'news/home.html')
    return res

def contactUs(request):
    if request.method=="POST":
        F_Name=request.POST['fName']
        L_Name=request.POST['lName']
        state=request.POST['state']
        city=request.POST['city']
        add=request.POST['address']
        email=request.POST['mail']

        if len(F_Name)<2 or len(L_Name)<3 or len(email)<12:
            messages.error(request,"Please Fill the Form Correctly ")
        else:
            contact=Contact(PFirstName=F_Name,PLastName=L_Name,PAddress=add,PState=state,PCity=city,PEmail=email)
            contact.save()
            messages.success(request,"Your Form is Submitted Succesfully ")
            return render(request,'news/contactUs.html',{"name":F_Name})
    return render(request,'news/contactUs.html')

def allNews(request,slug):
    url = (f"https://newsapi.org/v2/everything?q={slug}&apiKey={apiKey}")
    news = requests.get(url).text
    news_dict=json.loads(news)
    arts=news_dict['articles']
    res=render(request,'news/newsView.html',{"arts":arts})
    return res

def search(request):
    value=request.GET.get('text')

    url = (f"https://newsapi.org/v2/everything?q={value}&apiKey={apiKey}")
    news = requests.get(url).text
    news_dict=json.loads(news)
    arts=news_dict['articles']
    return render(request,'news/newsView.html',{"arts":arts})




def latNews(request):
    url = (f"http://newsapi.org/v2/top-headlines?country=in&apiKey={apiKey}")
    news = requests.get(url).text
    news_dict=json.loads(news)
    arts=news_dict['articles']

    res=render(request,'news/newsView.html',{"arts":arts})
    return res
