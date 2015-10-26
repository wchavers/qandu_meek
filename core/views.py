from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

# Create your views here.
class Home(TemplateView):
    template_name = "home.html"

class ContactCreateView(CreateView):
    model = Contact
    template_name = "contact/contact_form.html"
    fields = ['title','first_Name', 'last_Name', 'email_Address', 'message']
    success_url = reverse_lazy('success')
    
class AboutCreateView(CreateView):
  template_name = "about.html"

class Success(TemplateView):
     template_name = "success.html"
