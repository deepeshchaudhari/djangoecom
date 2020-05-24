from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category  =models.CharField(max_length=50,default="")
    subcategory  = models.CharField(max_length=50,default="")
    price  =models.IntegerField(default=0)
    desc = models.CharField(max_length=3000)
    pub_date = models.DateField()
    image = models.FileField(upload_to="shop/images",default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email  =models.CharField(max_length=70,default="")
    username  =models.CharField(max_length=30,default="")
    address  =models.CharField(max_length=100,default="")
    contact  =models.CharField(max_length=12,default="")

    def __str__(self):
        return self.firstname