# This part is used for import relevant libraries or some class or functions form other files in this project.
import datetime

from django.test import TestCase

from core.models import User
from product.models import Category, Manufacturer, CategoryAttributeValue, ProductAttribute, Price, Discount
from ..models import *


# Product App Models Test
class ProductApp(TestCase):

    def setUp(self) -> None:
        self.category_model_1 = Category.objects.create(id=1, category_name='Digital Product', depth=1)
        self.category_model_2 = Category.objects.create(id=2, category_name='Mobile', depth=2,
                                                        parent_category=self.category_model_1)
        self.manufacturer_model = Manufacturer.objects.create(id=1, manufacturer_name='Apple')
        self.product_model = Products.objects.create(id=1, product_name="IPhone 6", product_description="test",
                                                     manufacturer_id=self.manufacturer_model,
                                                     category_id=self.category_model_2)
        self.category_attribute_value_model = CategoryAttributeValue.objects.create(id=1,
                                                                                    category_id=self.category_model_2,
                                                                                    attribute_name='os',
                                                                                    attribute_value='ios',
                                                                                    attribute_description='test')
        self.product_attribute_model = ProductAttribute(products_id=self.product_model,
                                                        category_attribute_value_id=self.category_attribute_value_model,
                                                        price_adjustment=10, is_fixed=True, is_available=True)
        self.price_model = Price.objects.create(products_id=self.product_model, price=30000000, is_used=True,
                                                start_date='2020-08-12',
                                                end_date='2020-08-19')
        self.discount_model = Discount.objects.create(products_id=self.product_model, discount=5,
                                                      discount_name='summer', is_fixed=True,
                                                      start_date='2021-02-01', end_date='2021-02-04')

        self.user_model = User.objects.create(id=1, first_name='Sasan', last_name='Sohrabi',
                                              email='sasan.sp92@hotmail.com',
                                              phone='09195145937', is_active=True, is_staff=False)
        self.user_model.set_password('123456')
        self.user_model.save()

        self.customer_model = Customer.objects.create(user=self.user_model, national_code=5170040271,
                                                      birth_day='1992-02-08')

        self.order_model = Ordered.objects.create(id=1, customer_id=self.customer_model,
                                                  purchase_date=datetime.datetime.now(tz=datetime.timezone.utc))
        self.suborder_model_1 = OrderedProduct.objects.create(id=1, product_id=self.product_model,
                                                              order_id=self.order_model, quantity=10)
        self.suborder_model_2 = OrderedProduct.objects.create(id=2, product_id=self.product_model,
                                                              order_id=self.order_model, quantity=5)

    def test_order_order_name_label(self):
        print(datetime.datetime.now(tz=datetime.timezone.utc))
        order_model = self.order_model.__class__.objects.get(id=1)
        field_label = order_model._meta.get_field('customer_id').verbose_name
        self.assertEqual(field_label, 'Customer')

    def test_order_product_object_name_is_correct(self):
        suborder_model_1 = self.suborder_model_1.__class__.objects.get(id=2)
        expected_object_name = f"{suborder_model_1.id}# Product Name: {suborder_model_1.product_id.product_name}," \
                               f" OrderId: {suborder_model_1.order_id.id}, CustomerId: {suborder_model_1.order_id.customer_id}"

        self.assertEqual(str(suborder_model_1), expected_object_name)

    def test_category_depth(self):
        category_model = self.category_model_1.__class__.objects.get(id=2)
        if category_model.parent_category:
            self.assertGreaterEqual(category_model.depth, 2)
        else:
            self.assertEqual(category_model.depth, 1)

    def test_manufacturer_manufacturer_name_label(self):
        manufacturer_model = self.manufacturer_model.__class__.objects.get(manufacturer_name='Apple')
        field_label = manufacturer_model._meta.get_field('manufacturer_name').verbose_name
        self.assertEqual(field_label, 'Manufacturer Name')

    def test_manufacturer_manufacturer_name_max_length(self):
        manufacturer_model = self.manufacturer_model.__class__.objects.get(id=1)
        field_label = manufacturer_model._meta.get_field('manufacturer_name').max_length
        self.assertEqual(field_label, 100)

    def test_manufacturer_object_name_is_correct(self):
        manufacturer_model = self.manufacturer_model.__class__.objects.get(id=1)
        expected_object_name = f"{manufacturer_model.id}# Manufacturer Name: {manufacturer_model.manufacturer_name}"
        self.assertEqual(str(manufacturer_model), expected_object_name)

    def test_final_price_positive(self):
        final_price = self.discount_model.__class__.objects.get(id=1).final_price()
        self.assertGreaterEqual(final_price, 0)

    def test_final_price_greater_than_discount(self):
        price = self.price_model.__class__.objects.get(id=1).price
        discount = self.discount_model.__class__.objects.get(id=1).discount
        self.assertGreaterEqual(price, discount)
