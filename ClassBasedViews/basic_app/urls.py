from django.urls import path, re_path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('schools/', views.SchoolListView.as_view(), name='schools'),
    re_path('schools/(?P<pk>\d+)', views.SchoolDetailView.as_view(), name='detail'),
    path('schools/create/', views.CreateSchoolView.as_view(), name='create'),
    re_path('schools/update/(?P<pk>\d+)', views.UpdateSchoolView.as_view(), name='update'),
    re_path('schools/delete/(?P<pk>\d+)', views.DeleteSchoolView.as_view(), name='delete'),
    re_path('schools/(?P<pk>\d+)/addstudent', views.CreateStudentView.as_view(), name='add_student'),
    path('basicview/', views.MyClassBasedView.as_view(), name='naiveView'),
    path('templateview/', views.MyTemplateView.as_view(), name='templateView'),
]
