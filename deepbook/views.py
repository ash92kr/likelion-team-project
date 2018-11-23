from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'
    
class TeamPage(TemplateView):
    template_name = 'ourteam.html'
    
class ContactPage(TemplateView):
    template_name = 'contact.html'