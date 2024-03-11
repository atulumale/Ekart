from django.contrib import admin
from ecomapp.models import Product,Cart,Order

# Register your models here.

# admin.site.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'pdetails', 'price', 'cat', 'is_active',]
    list_filter = ['cat', 'is_active']

admin.site.register(Product, ProductAdmin)
admin.site.register(Cart)
admin.site.register(Order)