from django.db import models

class Coldbean(models.Model):
    time_now = models.TextField()
    title = models.CharField(max_length=255)
    times = models.TextField()
