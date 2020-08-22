from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from basic_app import models

# Create your views here.

class IndexView(TemplateView):
    template_name = 'basic_app/index.html'

class SchoolListView(ListView):
    #default context_object_name is model name in lowercase_list, here = school_list
    context_object_name = 'schools'
    model = models.School

class SchoolDetailView(DetailView):
    template_name = 'basic_app/school_detail.html'

    #default context_object_name is model name in lowercase, here = school
    context_object_name = 'school_detail'
    model = models.School

class CreateSchoolView(CreateView):
    fields = ('name', 'principal', 'location')
    model = models.School

class UpdateSchoolView(UpdateView):
    fields = ('principal', 'location')
    model = models.School

class DeleteSchoolView(DeleteView):
    #default context_object_name is model name in lowercase, here = school
    model = models.School
    success_url = reverse_lazy("basic_app:schools")

class CreateStudentView(CreateView):
    fields = ('name', 'age')
    model = models.Student

class MyClassBasedView(View):
    def get(self, request):
        return HttpResponse("Whoa class based view is working! Yes indeed!")

class MyTemplateView(TemplateView):
    template_name = 'mytemplate.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['injectme'] = "Yes fam! I am the injected one!"
        return context
