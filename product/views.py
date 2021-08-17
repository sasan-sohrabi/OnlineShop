from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views import View, generic
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from order.models import OrderedProduct, Ordered
from product.models import *
from product.serializers import ProductSerializer


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'special_products'
    model = Products


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'category.html', {'category': category})


class ProductCardView(DetailView):
    template_name = 'product.html'
    model = Products
    context_object_name = 'product'
    slug_field = 'slug'
    slug_url_kwarg = 'product_slug'

    def get_context_data(self, **kwargs):
        context = super(ProductCardView, self).get_context_data(**kwargs)
        if str(self.request.user) != 'AnonymousUser':
            context['orderItem'] = OrderedProduct.objects.filter(order_id__customer_id__user=self.request.user)
        return context








