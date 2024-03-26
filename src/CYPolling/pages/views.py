# added to turn function for custom homepage into DJANGO friendly code
from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.

# a place to handle various web pages

# Functions or classes

# define home page
def homepage_view(request, *args, **kwargs):
   # return HttpResponse("<h1>Hello World</h1>")
   
   # IN ORDER TO ACTUALLY REQUEST HTML DOCUMENT
   print(args, kwargs)
   print(request.user)
   return render(request, "home.html", {}) # # FIRST QUOTE ARG IS A TEMPLATE URL, THEN ADD EMPTY DICTIONARY FOR CONTEXT 



# MUST TURN INTO DJANGO FRIENDLY CODE >>> IMPORT httpresponse >> wrap in HttpResponse


# CREATING MORE PAGES

def contact_View(request, *args, **kawrgs):
    return HttpResponse("<h1>Contact Page</h1>")






def about_View(*args, **kawrgs):        # # MUST ADD REQUEST AS BEGINNING ARGUMENT
    return HttpResponse("<h1>Contact Page</h1>")


def extra_View(*args, **kawrgs):
    return HttpResponse("<h1>Extra Page</h1>")

def social_View(*args, **kawrgs):
    return HttpResponse("<h1>Social Page</h1>")