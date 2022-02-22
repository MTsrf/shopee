from django.contrib import admin
from . models import (Customer, Product, Cart, OrderPlaced)



@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'zipcode', 'name', 'locality', 'city', 'state')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id','title','selling_price','discounted_price','description','brand','category','product_image')

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ('user','product','quantity')

@admin.register(OrderPlaced)
class OrederPlacedModelAdmin(admin.ModelAdmin):
    list_display = ('id','user','customer','product','quantity','ordered_date','status')
# Register your models here.
