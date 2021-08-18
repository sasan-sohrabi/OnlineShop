# Generated by Django 3.2.5 on 2021-08-18 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='owner',
            field=models.ForeignKey(help_text='Owner of Address', on_delete=django.db.models.deletion.CASCADE, related_name='addresses', to=settings.AUTH_USER_MODEL, verbose_name='Owner'),
        ),
    ]
