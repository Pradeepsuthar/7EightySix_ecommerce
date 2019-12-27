from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField(default=0)
    main_product_category = models.CharField(max_length=50, default="")
    product_category = models.CharField(max_length=50, default="")
    product_sub_category = models.CharField(max_length=50, default="")
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")
    offers = models.IntegerField(default=0)
    size = models.CharField(max_length=10,default="M")
    color = models.CharField(max_length=50,default="Black")
    material = models.CharField(max_length=50,default="Material")

    def __str__(self):
        return self.product_name