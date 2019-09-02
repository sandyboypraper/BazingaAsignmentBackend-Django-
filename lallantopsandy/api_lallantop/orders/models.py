from django.db import models

# Create your models here.
class orders(models.Model):

    def __str__(self):
        return str(self.itemname)

    itemname = models.CharField(max_length = 200, default=' ')
    quantity = models.IntegerField( default='9')
    price  = models.CharField(max_length = 200, default=' ')


    customername = models.CharField(max_length = 200,  default=' ')
    contact = models.CharField(max_length=15 ,  default='3')
