from django.db import models

# Create your models here.

# # We want these mapped to database
# #  Must inherit Model from models

#Going to map to the database

class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()