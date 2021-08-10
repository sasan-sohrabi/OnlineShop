# This part is used for import relevant libraries or some class or functions form other files in this project.
from django.core.validators import *
from django.db import models
from core.models import BaseModel, User
from django.utils.translation import gettext_lazy as _


class Customer(BaseModel):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name=_("Customer"),
                             help_text=_("Customer Id"))
    national_code = models.IntegerField(verbose_name=_("National Code"),
                                        validators=[RegexValidator(regex=r'^[0-9]{10}$',
                                                                   message=_('National Code Is Not Correct!'))],
                                        null=True,
                                        help_text=_("National Code of Customer"), )
    birth_day = models.DateField(verbose_name=_("Birth Day"), null=True, help_text=_("Birth Day of Customer"))

    def __str__(self):
        return f"{self.id}# Customer Full Name: {self.user.first_name} {self.user.last_name}"