from django.urls import path
from .views import DoorLogList, DeviceLogList, DoorLogPostHandler
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'api_main'
urlpatterns = [
    path('doorlogs/', DoorLogList.as_view(), name='doorlogs'),
    path('devicelogs/', DeviceLogList.as_view(), name='devicelogs'),
    path('gerkon/', DoorLogPostHandler.as_view(), name='gerkon')
    ]

urlpatterns = format_suffix_patterns(urlpatterns)