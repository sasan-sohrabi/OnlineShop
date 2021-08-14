from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'products'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<slug:category_slug>/', category_list, name='category'),
    path('<slug:category_slug>/<slug:product_slug>/', ProductCardView.as_view(), name='product')
    # path('product_api/', product_list_view)
]
