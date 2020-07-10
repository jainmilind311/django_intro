from django.urls import path
from handler import views

app_name = 'handler'

urlpatterns = [
    path('', views.index, name='index'), 
    path('register/', views.register, name='register'), 
    path('contact/', views.contact, name='contact'), 
]
