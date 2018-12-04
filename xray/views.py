from django.shortcuts import render, redirect, resolve_url
from django.views.generic import TemplateView, CreateView, ListView, DetailView, DeleteView
from .models import Xray
from .diagnosis import Model
from django.urls import reverse_lazy

from keras.models import load_model
import cv2

# Create your views here.
class XrayIndex(TemplateView):
    template_name = 'xray/xray_index.html'

class XrayCreate(CreateView):
    model = Xray
    fields=['image',]

class XrayList(ListView):
    model = Xray
    fields = ('image')
    success_url = reverse_lazy('xray:list')

class XrayDetail(DetailView):
    model = Xray

class XrayDelete(DeleteView):
    model = Xray
    success_url = reverse_lazy('xray:list')
    

def XrayDiagnosis(request, pk):
    img = Xray.objects.get(id = pk)
    path = '/home/ubuntu/workspace/DeepBook' + img.image.url
    re_img, per, label = Model(path)
    new_path = './xray/media/{}.jpg'.format(pk)
    new_path1 = './media/image/new_img/{}.jpg'.format(pk)
    new_path2 = '/media/image/new_img/{}.jpg'.format(pk)
    cv2.imwrite(new_path1, re_img)
    
    return render(request, 'xray/xray_diagnosis.html', {'path': new_path2, 'per' : per, 'label' :label})
