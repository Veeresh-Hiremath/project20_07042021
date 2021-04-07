from django.shortcuts import render
from django.http import HttpResponse
def index(request,data):
    return HttpResponse(f"<h1>user is entered the is {data}</h1>")

# Create your views here.
