from django.urls import path
from input_form import views


urlpatterns = [
    path('', views.index, name='index'), 
    path('form/', views.form_page, name='form'), 
]
