from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.utils import json

from customer.models import Customer
from order.models import Ordered, OrderedProduct
from product.models import Products


def update_item(request):
    data = json.loads(request.body.decode('utf-8'))
    product_id = data['productId']
    action = data['action']

    customer = Customer.objects.get(user=request.user)
    product = Products.objects.get(id=product_id)
    order = Ordered.objects.get_or_create(customer_id=customer, complete=False)[0]
    order_item = OrderedProduct.objects.get_or_create(order_id=order, product_id=product)[0]

    if action == 'add':
        order_item.quantity = (order_item.quantity + 1)

    elif action == 'remove':
        order_item.quantity = (order_item.quantity - 1)

    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()




    return JsonResponse('Item was added', safe=False)
