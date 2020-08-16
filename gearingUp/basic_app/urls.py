from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('usr_login/', views.usr_login, name='login'),
    path('usr_logout/', views.usr_logout, name='logout'), 
]
