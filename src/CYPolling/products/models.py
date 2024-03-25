from django.db import models

# Create your models here.

# # We want these mapped to database
# #  Must inherit Model from models

# # Must:
#  #        python manage.py makemigrations and python manage.py migrate when altered!!!! 

# # -------------------------- DO NOT ---- DELETE DATABASE ------------------------------------------
# # --------- DELETING DATABASE MAKES BAD THINGS HAPPEN AND TAKES THE SERVER WITH IT

class Product(models.Model):
    title       = models.CharField(max_length=120)  # max length is  R E Q U I R E D 
    description = models.TextField(blank=True, null=True)
    salary      = models.IntegerField()
    rating      = models.PositiveSmallIntegerField() # 32767 #default='3'