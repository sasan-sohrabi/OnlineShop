from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from product.models import Products
from product.serializers import ProductSerializer


class LandingView(ListView):
    template_name = 'index.html'
    context_object_name = 'special_products'
    model = Products

@csrf_exempt
def product_list_view(request):
    if request.method == 'GET':
        product = Products.objects.all()
        p = ProductSerializer(product, many=True)
        return JsonResponse({'products': p.data})

    if request.method == 'POST':
        p = ProductSerializer(data=request.POST)
        if p.is_valid():
            p.save()
            return JsonResponse(p.data)
        else:
            return JsonResponse(p.errors, status=400)


