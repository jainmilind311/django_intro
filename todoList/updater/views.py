from django.shortcuts import render
from updater import forms
from updater.models import Item
from datetime import date
# Create your views here.

def index(request):
    return to_do(request)


def to_do(request):
    current_tasks = Item.objects.order_by()
    new_task = forms.TaskForm()
    
    #NOT Completed!!
    if(request.method=='POST'):
        new_task = forms.TaskForm(request.form)
        
        if new_task.is_valid():
            added_task = new_task.save(commit=True)
            added_task.completed = False
            added_task.date = date.today()

        





    
