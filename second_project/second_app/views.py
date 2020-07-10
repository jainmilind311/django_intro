from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def index(request):
    return HttpResponse('<em>Hey! This is the second one.</em>')