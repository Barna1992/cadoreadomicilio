from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, UpdateView, DeleteView, CreateView
from django.views.generic.edit import FormView
from locali.forms import LocaleForm

def index(request):
    return render(request, 'frontend/index.html')

def about(request):
    return render(request, 'frontend/about.html')

class LocaleFormView(FormView, CreateView):
    template_name = 'frontend/create.html'
    form_class = LocaleForm
    success_url = '/'
