from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def index(request):
    obj=Portfolio.objects.all()[0]
    return render(request,"index.html",context={'obj':obj})