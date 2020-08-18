from django.db import models
from .product import Product
from .customer import Customer
import datetime
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=50, default='', blank=True)
    date = models.DateField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)
    completion_date = models.DateField(null= True)

    class order_status(models.TextChoices):
        PENDING = 'PE',_('Pending')
        ACCEPTED = 'AC',_('Accepted')
        DELIVERY = 'DE',_('Delivery')
        COMPLETED = 'CO',_('Completed')
    order_state = models.CharField(max_length= 3,
    choices=order_status.choices,
    default=order_status.PENDING)

    class delivery_method(models.TextChoices):
        CASHONDELIVERY = 'COD',_('CashOnDelivery')
        PREPAID = 'PAID',_('PREPAID')
    delivery_type = models.CharField(max_length=4,
    choices=delivery_method.choices,
    default=delivery_method.CASHONDELIVERY)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer=customer_id).order_by('-date')

