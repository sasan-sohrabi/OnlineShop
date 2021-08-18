from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'account'

urlpatterns = [
    path('profile/', CustomerView.as_view(), name='profile'),
    path('profiel-addtional-info/', update_customer, name='updateCustomer'),

    path('users/', UserListApi.as_view(), name='user'),
    path('users/<int:pk>', UserDetailApi.as_view(), name='users'),

    path('address/', AddressListApi.as_view(), name='address'),
    path('address/<int:pk>', AddressDetailApi.as_view(), name='addresses'),

    path('customers/', CustomerListApi.as_view(), name='customers'),
    path('customers/<int:pk>', CustomerDetailApi.as_view(), name='customer'),
]
