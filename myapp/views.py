from cgitb import text
import imp
import re
from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html')

def counter(request):
    text = request.GET['text']
    return render(request, 'counter.html')

