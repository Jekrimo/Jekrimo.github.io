from django.shortcuts import render, redirect

def index(request):
    return render(request, "portfoliosite/index.html")

def show(request):
    return render(request, "portfoliosite/show.html")
