from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"
    
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class ContactCreateView(CreateView):
    model = Contact
    template_name = "contact/contact_form.html"
    fields = ['title', 'description']
    success_url = reverse_lazy('home')