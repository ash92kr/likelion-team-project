from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class XrayIndex(TemplateView):
    template_name = 'xray/xray_index.html'