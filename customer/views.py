from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.views.generic import DetailView, UpdateView, ListView
from rest_framework import generics, permissions

from core.models import User, Address
from customer.forms import UserForm, CustomerForm
from customer.models import Customer
from customer.permisssions import IsOwner
from customer.serializers import UserSerializer, UserBriefSerializer, AddressSerializer, CustomerSerializers, \
    CustomerSerializers_1


class CustomerView(ListView):
    template_name = 'profile.html'
    model = Customer
    context_object_name = 'customer'

    def get_queryset(self):
        return Customer.objects.get(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(CustomerView, self).get_context_data(**kwargs)
        context['customer_user'] = User.objects.get(id=self.request.user.id)
        return context


def update_customer(request):
    instance_user = User.objects.get(id=request.user.id)
    instance_customer = Customer.objects.get(user_id=request.user.id)

    user_form = UserForm(request.POST or None, instance=instance_user)
    customer_form = CustomerForm(request.POST or None, instance=instance_customer)

    if request.method == 'POST':
        if user_form.is_valid() and customer_form.is_valid():
            user_update = user_form.save()
            customer_update = customer_form.save(user_update)

            return redirect('account:profile')

    context = {'user_form': user_form, 'customer_form': customer_form, 'user_instance': instance_user}
    return render(request, 'profile-additional-info.html', context)


# Api Views

class UserListApi(generics.ListAPIView):
    serializer_class = UserBriefSerializer
    queryset = User.objects.all()
    permission_classes = [
        permissions.IsAdminUser
    ]


class UserDetailApi(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)


class AddressListApi(generics.ListCreateAPIView):
    serializer_class = AddressSerializer

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return Address.objects.filter(owner=self.request.user)


class AddressDetailApi(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    permission_classes = [
        IsOwner
    ]


class CustomerListApi(generics.ListAPIView):
    serializer_class = CustomerSerializers_1
    queryset = Customer.objects.all()

    # permission_classes = [
    #     permissions.IsAdminUser
    # ]


class CustomerDetailApi(generics.RetrieveUpdateAPIView):
    serializer_class = CustomerSerializers_1
    queryset = Customer.objects.all()

    # permission_classes = [
    #     permissions.IsAdminUser
    # ]

    # def get_queryset(self):
    #     return Customer.objects.filter(id=self.request.user.id)
