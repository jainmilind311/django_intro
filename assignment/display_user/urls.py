from django.urls import path
from display_user import views



urlpatterns = [
    path('', views.index, name='index'), 
    path('data/', views.data, name='data'), 
]
