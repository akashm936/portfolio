from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request,"base.html")

def project(request):
    return render(request,"project.html")

def contact(request):
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def jointeam(request):
    return render(request,"jointeam.html")
      