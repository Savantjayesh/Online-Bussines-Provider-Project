from django.db import models

# Create your models here.
CATEGORY_CHOICES = {
    ('pd','Papad'),
    ('ck','Cakes'),
    ('pr','PuranPoli'),
}
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    Product_image = models.ImageField(upload_to='Product')

    def __str__(self):
        return self.title
class Signup(models.Model):
    first_name = models.CharField(max_length=15,blank=False,null=False)
    middle_name = models.CharField(max_length=15,blank=False,null=False)
    last_name = models.CharField(max_length=15,blank=False,null=False)
    contact = models.IntegerField(blank=False,null=False)
    birth_date =models.DateField(null=True)
    user_name = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50,blank=False,null=False)
    
    def __str__(self):
        return self.first_name
        


class About(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_no = models.IntegerField()
    query = models.CharField(max_length=100,null=False,blank=False)

    def __str__(self):
        return self.name
