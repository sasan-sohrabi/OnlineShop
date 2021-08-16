from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'orders'

urlpatterns = [
    path('update_item/', update_item, name='updateItem')
]