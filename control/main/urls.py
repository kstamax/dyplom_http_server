from django.urls import path
from .views import IndexPageView, CommandLinePageView, LogsPageView, LoginPageView
from django.contrib.auth.views import LogoutView

app_name = 'main'
urlpatterns = [
    path('',IndexPageView.as_view(),name='index'),
    path('console',CommandLinePageView.as_view(),name='console'),
    path('login',LoginPageView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='main:login'), name='logout'),
    path('clogs',LogsPageView.as_view(),name='c_logs')

]
