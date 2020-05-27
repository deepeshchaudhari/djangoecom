# Generated by Django 3.0.6 on 2020-05-25 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20200522_0653'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.IntegerField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('Zip_code', models.CharField(max_length=100)),
            ],
        ),
    ]