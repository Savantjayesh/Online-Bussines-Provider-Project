from django.contrib import admin
from home.models import Product
from home.models import Signup
from home.models import About
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price','selling_price', 'category', 'Product_image']


@admin.register(Signup)
class SignupModelAdmin(admin.ModelAdmin):
        list_display = ['first_name', 'middle_name', 'last_name','contact', 'birth_date', 'user_name','password']

@admin.register(About)
class AboutModelAdmin(admin.ModelAdmin):
        list_display = ['name','email','phone_no','query']


