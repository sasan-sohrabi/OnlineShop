# This part is used for import relevant libraries or some class or functions form other files in this project.
from django.test import TestCase
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

    def test_category_category_name_label(self):
        category_model = self.category_model_2.__class__.objects.get(category_name='Mobile')
        field_label = category_model._meta.get_field('category_name').verbose_name
        self.assertEqual(field_label, 'Category Name')

    def test_category_category_name_max_length(self):
        category_model = self.category_model_1.__class__.objects.get(id=1)
        field_label = category_model._meta.get_field('category_name').max_length
        self.assertEqual(field_label, 100)

    def test_category_object_name_is_correct(self):
        category_model = self.category_model_1.__class__.objects.get(id=2)
        expected_object_name = f"{category_model.id}# Category Name: {category_model.category_name}"
        self.assertEqual(str(category_model), expected_object_name)

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
