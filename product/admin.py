from django.contrib import admin

from product.models import Product

# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['picture', 'name', 'price',
                    'status', 'created_at', 'updated_at', 'user']
    list_editable = ['price', 'status']
    list_filter = ['price', 'status', 'created_at']
    list_per_page = 10

