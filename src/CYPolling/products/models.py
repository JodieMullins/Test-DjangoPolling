from django.db import models

# Create your models here.

# # We want these mapped to database
# #  Must inherit Model from models

# # Must:
#  #        python manage.py makemigrations and python manage.py migrate when altered!!!! 

class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    salary      = models.TextField()
    rating      = models.TextField(default='3')