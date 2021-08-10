from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'list_view'

urlpatterns = [
    path('', LandingView.as_view(), name='landing'),
    path('<int:pk>', ProductCardView.as_view(), name='pname')
    # path('product_api/', product_list_view)
]