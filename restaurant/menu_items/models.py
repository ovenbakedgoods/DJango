from django.db import models

class Menu(models.Model):
    entree = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.entree
        return self.description

class Step(models.Model):
    nutritioninfo = models.TextField()
    #price = models.TextField()
    order = models.IntegerField(default=0)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)




    def __str__(self):
        return self.price
        return self.nutritioninfo
 
class Meta:
    ordering = ['order', ]

       

   

    

