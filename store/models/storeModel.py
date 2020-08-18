from django.db import models
from .customer import Customer
import datetime

class storeModel(models.Model):
    storeName = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.now)
    tagLine = models.CharField(max_length=50, default='', blank=True)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/stores/',blank = True)

    def placeOrder(self):
        self.save()
