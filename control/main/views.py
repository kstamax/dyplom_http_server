from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView

# Create your views here.

#login
class LoginPageView(LoginView):
    template_name = 'main/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('main:index')

#main page
class IndexPageView(LoginRequiredMixin, TemplateView):
    template_name = 'main/index.html'

class LogsPageView(LoginRequiredMixin, TemplateView):
    template_name = 'main/c_logs.html'

class ControlDevicePageView(LoginRequiredMixin, TemplateView):
    template_name = 'main/control_device.html'