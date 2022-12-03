from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import DoorLogSerializer, DeviceLogSerializer

from .models import DoorLog, DeviceLog

class DoorLogList(generics.ListAPIView):
    serializer_class = DoorLogSerializer
    def get_queryset(self):
        return DoorLog.objects.all().order_by("-log_date")

class DeviceLogList(generics.ListAPIView):
    serializer_class = DeviceLogSerializer
    def get_queryset(self):
        return DeviceLog.objects.all().order_by("-log_date")