# This part is used for import relevant libraries or some class or functions form other files in this project.
from django.core.validators import *
from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _

# Create your models here.
from customer.models import Customer
from product.models import Products


class Ordered(BaseModel):
    customer_id = models.ForeignKey(Customer, verbose_name=_("Customer"), help_text=_("Customer of Order"),
                                    on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(verbose_name=_("Date"), help_text=_("Date of Purchase"), null=True)
    # STATUS_CHOICES = (
    #     ('processing', 'PROCESS'),
    #     ('paid', 'PAID')
    # )
    # status_order = models.CharField(max_length=10, choices=STATUS_CHOICES, default='processing',
    #                                 verbose_name=_("Order Status"),
    #                                 help_text=_("Status of Order, example: processing, paid, ..."))
    complete = models.BooleanField(verbose_name=_("Order Status"), help_text=_("Status of Order, example: True, False, ..."), default=False)

    def __str__(self):
        return f"{self.id}#"


class OrderedProduct(BaseModel):
    product_id = models.ForeignKey(Products, verbose_name=_("Product"), help_text=_("Product of Order"),
                                   on_delete=models.CASCADE)
    order_id = models.ForeignKey(Ordered, verbose_name=_("Order"), help_text=_("Order of  SubOrder"),
                                 on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name=_("Quantity"), help_text=_("Quantity of  SubOrder"), default=0)

    def __str__(self):
        return f"{self.id}# Product Name: {self.product_id.product_name}, OrderId: {self.order_id.id}, CustomerId: {self.order_id.customer_id}"
