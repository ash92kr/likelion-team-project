# oauth/posts/views.py 참고함

from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from .models import Xray
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class XrayIndex(TemplateView):
    template_name = 'xray/xray_index.html'

class XrayCreate(CreateView):
    model = Xray
    fields=['image',]

class XrayList(LoginRequiredMixin, ListView):
    model = Xray
    fields = ('image')
    success_url = reverse_lazy('xray:list')

class XrayDetail(DetailView):
    model = Xray

class XrayDelete(DeleteView):
    model = Xray
    success_url = reverse_lazy('xray:list')
    

