from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, UpdateView

from core.models import User
from customer.models import Customer


class CustomerView(DetailView):
    template_name = 'profile.html'
    model = Customer
    context_object_name = 'customer'

    def get_queryset(self):
        return Customer.objects.get(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CustomerView, self).get_context_data(**kwargs)
        context['customer_user'] = User.objects.get(id=self.request.user)
        return context
