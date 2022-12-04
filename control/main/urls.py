from django.urls import path
from .views import IndexPageView, ControlDevicePageView, LogsPageView, LoginPageView, LedControlView, RelayControlView,ResetDeviceView
from django.contrib.auth.views import LogoutView

app_name = 'main'
urlpatterns = [
    path('',IndexPageView.as_view(),name='index'),
    path('control',ControlDevicePageView.as_view(),name='control_dev'),
    path('login',LoginPageView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='main:login'), name='logout'),
    path('clogs',LogsPageView.as_view(),name='c_logs'),
    path('led/<str:state>', LedControlView.as_view(), name='led'),
    path('relay/<str:state>', RelayControlView.as_view(), name='relay'),
    path('resetd', ResetDeviceView.as_view(), name='resetd')
]
