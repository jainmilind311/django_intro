from django.shortcuts import render
from updater import forms
from updater.models import Item
from datetime import date

# Create your views here.

def index(request):
    return to_do(request)


def to_do(request):

    new_task = forms.TaskForm()
    
    print('')
    if(request.method=='POST'):

        if request.POST.get('new_task_added'):
            print(str(request.POST))
            new_task = forms.TaskForm(request.POST)
            if new_task.is_valid():
                added_task = new_task.save(commit=True)


        else:
            task_to_delete = request.POST.get('delete_task')
            task = Item.objects.get(task=task_to_delete)
            task.delete()


    current_tasks = Item.objects.order_by('date')
    form_dict = {'task_form': new_task, 'current_tasks': current_tasks}
    return render(request, 'updater/todo.html', context=form_dict)

        





    
