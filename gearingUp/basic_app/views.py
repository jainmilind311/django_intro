from django.shortcuts import render
from basic_app import forms
# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required
def usr_logout(request):
    logout(request)
    return render(request, 'basic_app/index.html')
    # return HttpResponseRedirect(reverse('index'))

def index(request):
    return render(request, 'basic_app/index.html')

def register(request):

    registered=False
    if request.method == "POST":

        user_form = forms.UserForm(data=request.POST)
        user_profile_info_form = forms.UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and user_profile_info_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            user_profile_info = user_profile_info_form.save(commit=False)
            user_profile_info.user = user
            if 'profile_pic' in request.FILES:
                user_profile_info.profile_pic = request.FILES['profile_pic']
            user_profile_info.save()
            registered=True
        else:
            return print(user_form.errors, user_profile_info.errors)

    user_form = forms.UserForm()
    user_profile_info_form = forms.UserProfileInfoForm()

    dict = {
    'registered':registered,
    'user_form':user_form,
    'user_profile_info_form': user_profile_info_form
    }
    return render(request, 'basic_app/register.html', context=dict)

def usr_login(request):

    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
                # return render(request, 'basic_app/index.html')
            else:
                return HttpResponse("Account not active")
        else:
            print("Someone tried to login using these credentials")
            print("Username = {}, Password = {}".format(username, password))
            return HttpResponse("No such account was found. Please check the credentials again")

    else:
        return render(request, 'basic_app/login.html')
