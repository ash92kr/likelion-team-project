from django.views.generic import TemplateView, ListView, CreateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePage(TemplateView):
    template_name = 'index.html'
    
class TeamPage(TemplateView):
    template_name = 'ourteam.html'
    
class ContactPage(TemplateView):
    template_name = 'contact.html'
    
class DeepPage(TemplateView):
    template_name = 'deep.html'
    
class BookPage(TemplateView):
    template_name = 'book.html'    
    
    
class ServerPage(CreateView):   # Deep 서비스에서 사진을 입력하면 결과를 만듦
    model = Deep

class MyPage(LoginRequiredMixin, ListView):
    model = Deep  # Deep에서 사진을 입력해 만들어진 결과의 모델을 보여줌
     
