from django.contrib import admin

# Register your models here.

# # RELATIVE IMPORT
from .models import Product


admin.site.register(Product)