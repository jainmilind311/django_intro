from django.shortcuts import render
from my_app import forms
# Create your views here.

def index(request):
    return render(request, 'my_app/index.html')

def register_usr(request):
    my_form = forms.MyForm()

    if(request.method == 'POST'):
        my_form = forms.MyForm(request.POST)
        
        if my_form.is_valid():
            my_form.save(commit=True)
            return index(request)
        else:
            print('Invalid credentials!')
        

    form_dict = {'form': my_form}
    return render(request, 'my_app/register.html', context=form_dict)

