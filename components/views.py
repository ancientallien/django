from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django import forms
from django.urls import reverse_lazy
from django.urls import reverse
from urllib.parse import urlencode
from django.http import HttpResponseRedirect

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    #image = forms.ImageField()
    


class HomePageView(FormView):
    template_name = "components/index.html"
    form_class = ContactForm
    

    # def form_valid(self, form):
    #     # Save the form data
    #     # Redirect to the success page with form data as a query string
    #     return super().form_valid(form)
    
    def form_valid(self, form):
        # Handle the form submission
        # ...
        
        # Redirect to the success page with the form data in the query string
        success_url = reverse('about')
        form_data = form.cleaned_data
        query_params = '&'.join([f'{k}={v}' for k, v in form_data.items()])
        redirect_url = f'{success_url}?{query_params}'
        return HttpResponseRedirect(redirect_url)

    # def get_success_url(self):
    #     # Build the success URL with the form data as a query string
    #     success_url = reverse('about')
    #     query_string = self.request.GET.urlencode()
    #     if query_string:
    #         success_url += '?' + query_string
    #     return success_url

    def get_success_url(self):
        success_url = reverse('about')
        form_data = urlencode(self.request.GET.dict())
        return f'{success_url}?{form_data}'
        
    


class AboutPageView(TemplateView):  # new
    template_name = "components/about.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] =  self.request.GET['name']
        context['mail'] =  self.request.GET['email']
        #context['image'] =  self.request.GET['image']
        return context
    
    


class ResumePageView(TemplateView):  # new
    template_name = "components/resume.html"


class PortfolioPageView(TemplateView):  # new
    template_name = "components/port.html"


class ContactPageView(TemplateView):  # new
    template_name = "components/contact.html"
