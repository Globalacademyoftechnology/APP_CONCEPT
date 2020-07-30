from django.shortcuts import render
from django.http import HttpResponse
from math import factorial

# Create your views here.

def index(request):
    return HttpResponse("<h1>Welcome to Home Page</h1>")

def home(request):
    return render(request,"myapp/first.html",{"name":"Sneha Bhatt U"})

def fact1(request,val):
    n=int(val)
    return HttpResponse("<h2>The factorial is {} </h2>".format(factorial(n)))





