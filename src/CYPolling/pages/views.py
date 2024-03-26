# added to turn function for custom homepage into DJANGO friendly code
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

# a place to handle various web pages

# Functions or classes

# define home page
def homepage_view(*args, **kwargs):
    return HttpResponse("<h1>Hello World</h1>")



# MUST TURN INTO DJANGO FRIENDLY CODE >>> IMPORT httpresponse >> wrap in HttpResponse


# CREATING MORE PAGES

def contact_View(*args, **kawrgs):
    return HttpResponse("<h1>Contact Page</h1>")