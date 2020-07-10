from django.shortcuts import render

# Create your views here.

def another(request):
    return render(request, 'another_app/another.html')
