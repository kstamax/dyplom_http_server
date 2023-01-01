from django.db import models

# # Create your models here.
# class DoorLog(models.Model):
#     DOOR_STATES = (
#         ("opened","opened"),
#         ("closed","closed")
#     )
#     log_date = models.DateTimeField()
#     door_state = models.CharField(max_length=6, choices=DOOR_STATES)

# class DeviceLog(models.Model):
#     MESSAGE_TYPES = (
#         ("ERROR", "ERROR"),
#         ("INFO", "INFO")
#     )
#     log_date = models.DateTimeField()
#     message_type = models.CharField(max_length=10, choices=MESSAGE_TYPES)
#     message_body = models.TextField()

class TestModel(models.Model):
    DOOR_STATES = (
        ("opened","opened"),
        ("closed","closed")
    )
    log_date = models.DateTimeField()
    door_state = models.CharField(max_length=6, choices=DOOR_STATES)