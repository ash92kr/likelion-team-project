from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from .models import Xray
from django.urls import reverse_lazy

# Create your views here.
class XrayIndex(TemplateView):
    template_name = 'xray/xray_index.html'

class XrayCreate(CreateView):
    model = Xray
    fields=['image',]

class XrayList(ListView):
    model = Xray

class XrayDetail(DetailView):
    model = Xray

class XrayDelete(DeleteView):
    model = Xray
    success_url = reverse_lazy('xray:list')