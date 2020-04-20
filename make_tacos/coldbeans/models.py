from django.db import models

class Coldbean(models.Model):
    channel_up = models.TextField()
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return (self.title)

class Step(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField(default=0)
    bean = models.ForeignKey(Coldbean, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

