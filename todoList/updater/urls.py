from django.urls import path
from updater import views

app_name = 'updater'

urlpatterns = [
    path('', views.index, name='index'), 
    path('todo/', views.to_do, name='todoList')

]