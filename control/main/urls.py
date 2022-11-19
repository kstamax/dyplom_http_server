from django.urls import path
from .views import IndexPageView, CommandLinePageView, LogsPageView

app_name = 'main'
urlpatterns = [
    path('',IndexPageView.as_view(),name='index'),
    path('console',CommandLinePageView.as_view(),name='console'),
    path('clogs',LogsPageView.as_view(),name='c_logs')

]
