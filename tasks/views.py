from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request, opt = None):
    return HttpResponse("hello world")
