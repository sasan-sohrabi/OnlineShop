# This part is used for import relevant libraries or some class or functions form other files in this project.
from django.test import TestCase
from ..models import *


# Product App Models Test
class ProductApp(TestCase):

    def setUp(self) -> None:
        self.user_model = User.objects.create(id=1, first_name='Sasan', last_name='Sohrabi', email='sasan.sp92@hotmail.com',
                                              phone='09195145937', is_active=True, is_staff=False)
        self.user_model.set_password('123456')
        self.user_model.save()

        self.customer_model = Customer.objects.create(user=self.user_model, national_code=5170040271, birth_day='1992-02-08')

    def test_customer_name_label(self):
        customer_model = self.customer_model.__class__.objects.get(national_code=5170040271)
        field_label = customer_model._meta.get_field('national_code').verbose_name
        self.assertEqual(field_label, 'National Code')

    def test_customer_national_code_validator(self):
        customer_model = self.customer_model.__class__.objects.get(id=1)
        customer_model.national_code = 1231414183793697
        print(customer_model.national_code)
        customer_model.save()

    def test_customer_object_name_is_correct(self):
        customer_model = self.customer_model.__class__.objects.get(id=1)
        expected_object_name = f"{customer_model.id}# Customer Full Name: {customer_model.user.first_name} {customer_model.user.last_name}"
        self.assertEqual(str(customer_model), expected_object_name)

    def test_customer_password(self):
        user_model = self.user_model.__class__.objects.get(id=1)
        user_model.set_password('123456')
        user_model.save()
        print(user_model.password)
        self.assertTrue(user_model.check_password('123456'))
