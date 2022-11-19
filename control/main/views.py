from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# Create your views here.

#login
class LoginPageView():
    pass

#register
class RegisterPageView():
    pass

#main page
class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class LogsPageView(TemplateView):
    template_name = 'main/c_logs.html'

#command line for speaking with controller
class CommandLinePageView(TemplateView):
    template_name = 'main/console.html'