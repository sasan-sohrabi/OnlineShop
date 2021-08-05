from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Category)
admin.site.register(Manufacturer)
admin.site.register(Products)
admin.site.register(Price)
admin.site.register(Discount)
admin.site.register(CategoryAttributeValue)
admin.site.register(ProductAttribute)