from django.contrib import admin

from authentication.models import User

# Register your models here.
@admin.register(User)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone_number']
    list_editable = ['phone_number']
    list_filter = ['first_name','phone_number']
    list_per_page =10