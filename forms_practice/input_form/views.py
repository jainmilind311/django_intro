from django.shortcuts import render
from input_form import forms
# Create your views here.

def index(request):

    return render(request, 'input_form/index.html')


def form_page(request):
    my_form = forms.MyForm()

    if request.method == 'POST':
        my_form = forms.MyForm(request.POST)

    if my_form.is_valid():
        name = my_form.cleaned_data['name']
        email = my_form.cleaned_data['email']
        comments = my_form.cleaned_data['comments']
        
        
        

    form_dict = {'form': my_form}
    return render(request, 'input_form/input.html', context=form_dict)