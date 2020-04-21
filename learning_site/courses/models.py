from django.db import models


class Course(models.Model):
    Created_AT = models.DateTimeField(auto_now_add= True)
    title = models.CharField(max_length = 255)
    description = models.TextField()

    def __str__(self):
        return self.title
        return self.description
        return self.Created_AT

class Step(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    content = models.TextField(blank = True, default ="")
    order = models.IntegerField(default=0)
    course = models.ForeignKey(Course, on_delete= models.CASCADE)

class Meta:
    ordering = ['order',]

    def __str__(self):
        return self.title