from django.db import models


class Tutorial(models.Model):
    title = models.CharField(max_length=70, blank=False, default='')
    description = models.CharField(max_length=200,blank=False, default='')
    published = models.BooleanField(default=False)


class Service(models.Model):
    name_service = models.CharField(max_length=70, blank=False, default="0:30:00")
    small_time = models.TimeField(blank=False, default="0:30:00")
    medium_time = models.TimeField(blank=False, default="0:35:00")
    large_time = models.TimeField(blank=False, default="0:40:00")