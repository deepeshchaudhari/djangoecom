# Generated by Django 3.0.6 on 2020-05-26 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20200526_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='bill',
        ),
    ]
