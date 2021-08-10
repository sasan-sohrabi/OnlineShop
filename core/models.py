# This part is used for import relevant libraries or some class or functions form other files in this project.
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.validators import *
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

# Create BaseManager to use it for overriding some methods.
class BaseManager(models.Manager):

    # Override all queries for ignoring records that is logically deleted.
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)

    # Archive is used for all data include logical deleted data.
    def archive(self):
        return super().get_queryset()


# Create BaseModel to use it for all of others models in this project.
class BaseModel(models.Model):
    # Deleted attribute is used for logical delete.
    deleted = models.BooleanField(default=False)

    objects = BaseManager()

    class Meta:
        abstract = True


# This class is  just used for test BaseModel.
class TestModel(BaseModel):
    pass


# Create TimeStampMixin to add date of create, modify and delete from database.
class TimeStampMixin(BaseModel):
    create_timestamp = models.DateTimeField(auto_now_add=True)
    modify_timestamp = models.DateTimeField(auto_now=True)
    delete_timestamp = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True


class MyUserManager(UserManager):

    def create_superuser(self, username=None, email=None, password=None, **extra_fields):
        username = extra_fields['phone']
        return super().create_superuser(username, email, password, **extra_fields)


class User(AbstractUser):
    USERNAME_FIELD = 'phone'

    objects = MyUserManager()

    phone = models.CharField(max_length=20, unique=True, verbose_name=_("Phone Number"), validators=[
        RegexValidator(regex=r'^((\+98|0)9\d{9})$', message=_('Phone Number Is Not Correct!'))])

    GENDER_CHOICES = (
        ('male', 'MALE'),
        ('female', 'FEMALE'),
    )
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male', verbose_name=_("Gender"),
                              help_text=_("Gender of User, example: male or female"))

    def __str__(self):
        return f"{self.id}# User Name: {self.phone}, Full Name: {self.first_name} {self.last_name}"


class Address(BaseModel):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Owner"),
                              help_text=_("Owner of Address"))

    province = models.CharField(max_length=30, verbose_name=_("Province"),
                                help_text=_("Province of Address"))
    city = models.CharField(max_length=30, verbose_name=_("City"),
                            help_text=_("City of Address"))
    detail = models.CharField(max_length=200, verbose_name=_("Detail"),
                              help_text=_("Detail of Address"))

    def __str__(self):
        return f"{self.id}# User Name: {self.owner.username}, Full Name: {self.owner.first_name} {self.owner.last_name}," \
               f" Address: {self.province} - {self.city} - {self.detail}"
