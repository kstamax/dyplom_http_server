from django.urls import path
from .views import DoorLogList, DeviceLogList
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api_main'
urlpatterns = [
    path('doorlogs/', DoorLogList.as_view(), name='doorlogs'),
    path('devicelogs/', DeviceLogList.as_view(), name='devicelogs')
    ]

urlpatterns = format_suffix_patterns(urlpatterns)