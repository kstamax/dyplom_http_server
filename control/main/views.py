from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from api_main.models import DoorLog
import datetime as dt
from django.http import HttpResponse
from client_controller.send_commands import Esp
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

class LedControlView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            try:
                esp = Esp("192.168.0.108")
                state = kwargs['state']
                esp.change_led_state(state)
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e,status=500)
        else:
            return redirect('/login')

class RelayControlView(View):
    def get(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            try:
                esp = Esp("192.168.0.108")
                state = kwargs['state']
                esp.change_relay_state(state)
                return HttpResponse(status=204)
            except Exception as e:
                return HttpResponse(e,status=500)
        else:
            return redirect('/login')




