# Generated by Django 3.2.5 on 2021-08-16 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20210816_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordered',
            name='purchase_date',
            field=models.DateTimeField(blank=True, help_text='Date of Purchase', null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orderedproduct',
            name='quantity',
            field=models.IntegerField(default=0, help_text='Quantity of  SubOrder', verbose_name='Quantity'),
        ),
    ]