from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import DoorLogSerializer, DeviceLogSerializer
import datetime as dt
import logging

from .models import DoorLog, DeviceLog

class DoorLogList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DoorLogSerializer
    def get_queryset(self):
        return DoorLog.objects.all().order_by("-log_date")

class DeviceLogList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DeviceLogSerializer
    def get_queryset(self):
        return DeviceLog.objects.all().order_by("-log_date")

class DoorLogPostHandler(APIView):
    def post(self, request):
        serializer_data = {
            'log_date':'',
            'door_state':''
        }
        state = request.data['state']
        time_string = request.data['time']
        date_string = request.data['date']
        date_time_string = f'{date_string} {time_string}'
        serializer_data['log_date'] = dt.datetime.strptime(date_time_string,"%Y-%m-%d %H:%M:%S")
        if state == "1":
            serializer_data['door_state'] = 'opened'
        else:
            serializer_data['door_state'] = 'closed'
        serializer = DoorLogSerializer(data = serializer_data)
        if serializer.is_valid() and request.data['api_key']=='poberezhnyi':
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
