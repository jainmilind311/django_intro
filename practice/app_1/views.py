from django.shortcuts import render
from app_1.models import AccessRecord, Topic, Webpage
# Create your views here.

def index(request):
    
    my_dict = {'insert_me': 'This line is inserted dynamically'}

    return render(request, 'app_1/index.html', context=my_dict)


def show_data(request):

    records = AccessRecord.objects.order_by('last_access')
    access_dict = {'access_rec': records}

    return render(request, 'app_1/db.html', context=access_dict)


    