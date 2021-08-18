from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'orders'

urlpatterns = [
    path('update_item/', update_item, name='updateItem'),
    path('cart/', login_required(OrderView.as_view(), login_url='/login/'), name='orderItem'),

    path('orders/', OrderListApi.as_view(), name='orders'),
    path('orders/<int:pk>', OrderDetailApi.as_view(), name='order'),

    path('orderproducts/', OrderedProductListApi.as_view(), name='orderproducts'),
    path('orderproducts/<int:pk>', CustomerDetailApi.as_view(), name='orderproduct'),
]
