from django.shortcuts import render
from handler.forms import SignUpForm
# Create your views here.

def index(request):
    return render(request, 'handler/index.html')

def register(request):
    sign_up_form = SignUpForm()
    if(request.method=='POST'):
        sign_up_form_filled = SignUpForm(request.POST)
        sign_up_form_filled.save(commit=True)

    return render(request, 'handler/register.html', {'form': sign_up_form})

def contact(request):
    return render(request, 'handler/contact.html')