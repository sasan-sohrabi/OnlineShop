from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View, generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from product.models import *
from product.serializers import ProductSerializer


class LandingView(ListView):
    template_name = 'main_landing.html'
    context_object_name = 'special_products'
    model = Products

class ProductCardView(generic.DetailView):
    template_name = 'main_product.html'
    model = Products
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        print(kwargs)
        context = super().get_context_data(**kwargs)
        context['price'] = Discount.objects.get(id=self.object).final_price()
        return context


# class ProductCardView(generic.TemplateView):
#     template_name = 'main_product.html'
#     extra_context = {
#         'product': Products.objects.filter()
#     }

# @csrf_exempt
# def product_list_view(request):
#     if request.method == 'GET':
#         product = Products.objects.all()
#         p = ProductSerializer(product, many=True)
#         return JsonResponse({'products': p.data})
#
#     if request.method == 'POST':
#         p = ProductSerializer(data=request.POST)
#         if p.is_valid():
#             p.save()
#             return JsonResponse(p.data)
#         else:
#             return JsonResponse(p.errors, status=400)


