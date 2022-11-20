from rest_framework import serializers
from .models import DeviceLog, DoorLog

class DoorLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorLog
        fields = '__all__'

class DeviceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeviceLog
        fields = '__all__'