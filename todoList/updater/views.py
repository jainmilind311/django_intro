from django.shortcuts import render
from updater import forms
from updater.models import Item
from datetime import date

# Create your views here.

def index(request):
    return render(request, 'updater/index.html')



def to_do(request):

    if(request.method=='POST'):

        if request.POST.get('new_task_added'):
            # print(str(request.POST))
            new_task = forms.TaskForm(request.POST)
            if new_task.is_valid():
                added_task = new_task.save(commit=True)
                

        else:
            task_to_delete = request.POST.get('delete_task')
            task = Item.objects.get(task=task_to_delete)
            task.delete()

    
    new_task = forms.TaskForm()

    current_tasks = Item.objects.order_by('date')
    
    date_today = date.today()
    my_dict = {'task_form': new_task, 'current_tasks': current_tasks, 'date_today': date_today}
    return render(request, 'updater/todo.html', context=my_dict)

        
def notes(request):
    
    return render(request, 'updater/notes.html')




    
