from django.shortcuts import render
from display_user.models import User
# Create your views here.

def index(request):
    
    return render(request, 'display_user/index.html')



def data(request):
    usr_list = User.objects.order_by('first_name')
    user_dict = {'users': usr_list}
    return render(request, 'display_user/data.html', context=user_dict)