from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView
from .models import Xray

# Create your views here.
class XrayIndex(TemplateView):
    template_name = 'xray/xray_index.html'

class XrayCreate(CreateView):
    model = Xray
    fields=('image',)

class XrayList(ListView):
    model = Xray


    
    
# def read_img(request):
#     img = request.POST