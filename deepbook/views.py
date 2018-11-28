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
    
    