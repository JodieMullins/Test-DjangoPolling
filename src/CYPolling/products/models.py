from django.db import models

# Create your models here.

# # We want these mapped to database
# #  Must inherit Model from models

class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    salary      = models.TextField()
    rating      = models.TextField(default='3')