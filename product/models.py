# This part is used for import relevant libraries or some class or functions form other files in this project.
from django.core.validators import *
from django.db import models
from core.models import BaseModel
from django.utils.translation import gettext_lazy as _


# Create your models here.


class Category(BaseModel):
    category_name = models.CharField(verbose_name=_("Category Name"), max_length=100,
                                     help_text=_("Name of Category"))
    depth = models.PositiveSmallIntegerField(verbose_name=_("Depth"),
                                             help_text=_("Depth of category, include 1, 2 and 3"),
                                             validators=[MinValueValidator(1), MaxValueValidator(3)], null=True)
    category_url = models.FileField(verbose_name=_("Category Url"), upload_to='category_img/',
                                    help_text=_("Url of category images on os."),
                                    validators=[
                                        FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg', 'jpeg'])],
                                    default=None, null=True, blank=True)
    parent_category = models.ForeignKey('self', verbose_name=_("Parent Category"), on_delete=models.CASCADE,
                                        help_text=_("Category of Parent"), null=True, blank=True)

    class Meta:
        ordering = ['-depth']

    def __str__(self):
        return f"{self.id}# Category Name: {self.category_name}"


class Manufacturer(BaseModel):
    manufacturer_name = models.CharField(verbose_name=_("Manufacturer Name"), max_length=100,
                                         help_text=_("Name of Manufacturer, like: Samsung, LG and etc."))

    logo_url = models.FileField(verbose_name=_("Logo Url"), upload_to='manufacturer_logo/',
                                help_text=_("Url of manufacturer logo on os."),
                                validators=[FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg', 'jpeg'])],
                                default=None, null=True, blank=True)

    class Meta:
        ordering = ['manufacturer_name']

    def __str__(self):
        return f"{self.id}# Manufacturer Name: {self.manufacturer_name}"


class Products(BaseModel):
    product_name = models.CharField(verbose_name=_("Product Name"), max_length=100,
                                    help_text=_("Name of Product"))
    product_description = models.CharField(verbose_name=_("Product Description"), max_length=100,
                                           help_text=_("Description of product"), default=None, null=True, blank=True)
    manufacturer_id = models.ForeignKey(Manufacturer, verbose_name=_("Manufacturer"), on_delete=models.CASCADE,
                                        help_text=_("Manufacturer of Product"))
    product_url = models.FileField(verbose_name=_("Product Url"), upload_to='product_img/',
                                   help_text=_("Url of product images on os."),
                                   validators=[
                                       FileExtensionValidator(allowed_extensions=['gif', 'png', 'jpg', 'jpeg'])],
                                   default=None, null=True, blank=True)
    category_id = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE,
                                    help_text=_("Category of Product"))

    class Meta:
        ordering = ['product_name']

    def __str__(self):
        return f"{self.id}# Product Name: {self.product_name},Category Name: {self.category_id.category_name}," \
               f" Manufacturer Name: {self.manufacturer_id.manufacturer_name}"

    @classmethod
    def filter_by_category(cls, category):
        return cls.objects.filter(category_id__parent_category__category_name=category)




class CategoryAttributeValue(BaseModel):
    category_id = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.CASCADE,
                                    help_text=_("Category of Attribute"))
    attribute_name = models.CharField(verbose_name=_("Attribute Name"), max_length=100,
                                      help_text=_("Name of attribute"))
    attribute_description = models.CharField(verbose_name=_("Attribute Description"), max_length=100,
                                             help_text=_("Description of attribute"), default=None, null=True,
                                             blank=True)
    attribute_value = models.CharField(verbose_name=_("Value"), max_length=100,
                                       help_text=_("Value of attribute"))

    class Meta:
        ordering = ['attribute_name']

    def __str__(self):
        return f"{self.id}# Category Name: {self.category_id.category_name}," \
               f" Attribute Name: {self.attribute_name}, Attribute Value: {self.attribute_value}"

    @classmethod
    def filter_by_category(cls, category):
        return cls.objects.filter(category_id__parent_category__category_name=category)


class ProductAttribute(BaseModel):
    products_id = models.ForeignKey(Products, on_delete=models.CASCADE)
    category_attribute_value_id = models.ForeignKey(CategoryAttributeValue, verbose_name=_("Category"),
                                                    on_delete=models.CASCADE,
                                                    help_text=_("Category of Product"))
    price_adjustment = models.FloatField(verbose_name=_("Price Adjustment"),
                                         help_text=_("Adjustment of product price"))
    is_fixed = models.BooleanField(verbose_name=_("Percent Adjustment"),
                                   help_text=_("Adjustment of product price is percent."))
    is_available = models.BooleanField(verbose_name=_("Product Available"),
                                       help_text=_("IS Product Available?"))

    def __str__(self):
        return f"{self.id}# Product Name: {self.products_id.product_name}," \
               f" Category Name: {self.category_attribute_value_id.category_id.category_name}," \
               f" Attribute Name: {self.category_attribute_value_id.attribute_name}," \
               f" Attribute Value: {self.category_attribute_value_id.attribute_value}"

    @classmethod
    def filter_by_category(cls, product):
        return cls.objects.filter(products_id__product_name=product)


class Price(BaseModel):
    products_id = models.ForeignKey(Products, verbose_name=_("Product"),
                                    on_delete=models.CASCADE,
                                    help_text=_("Name of Product"))
    price = models.PositiveIntegerField(verbose_name=_("Price"), help_text=_("Price of Product"))
    is_used = models.BooleanField(verbose_name=_("Price Now"),
                                  help_text=_("Price that used in present time."))
    start_date = models.DateField(verbose_name=_("From Date"), help_text=_("From Date Price"))
    end_date = models.DateField(verbose_name=_("To Date"), help_text=_("To Date Price"))

    class Meta:
        ordering = ['price']

    def __str__(self):
        return f"{self.id}# Product Name: {self.products_id.product_name}," \
               f" Price: {self.price}, Price Now: {self.is_used}"


class Discount(BaseModel):
    products_id = models.ForeignKey(Products, verbose_name=_("Product"),
                                    on_delete=models.CASCADE,
                                    help_text=_("Name of Product"))
    discount = models.PositiveIntegerField(verbose_name=_("Discount"), help_text=_("Discount of Product"))
    discount_name = models.CharField(verbose_name=_("Discount Name"), max_length=100,
                                     help_text=_("Name of Discount"))
    is_fixed = models.BooleanField(verbose_name=_("Percent"),
                                   help_text=_("discount of product price is percent"))
    start_date = models.DateField(verbose_name=_("From Date"), help_text=_("From Date Discount"))
    end_date = models.DateField(verbose_name=_("To Date"), help_text=_("To Date Discount"))

    def __str__(self):
        return f"{self.id}# Product Name: {self.products_id.product_name}," \
               f" Discount Name: {self.discount_name}, Discount: {self.discount}"

    def final_price(self):
        if self.is_fixed:
            return Price.objects.get(id=self.products_id.id).price - self.discount * Price.objects.get(
                id=self.products_id.id).price * 0.01
        else:
            return Price.objects.get(id=self.products_id.id).price - self.discount
