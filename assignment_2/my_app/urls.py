from django.urls import path
from my_app import views


app_name = 'my_app'


urlpatterns = [
    path('', views.index, name='index'), 
    path('register/', views.register_usr, name='register'), 
]
