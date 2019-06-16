from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image,Location,Category


# Create your views here.
def welcome(request):
    image = Image.objects.all()
    return render(request, 'image.html',{'image':image})

 def view_by_location(request,location_name):
      
    images = Image.get_with_location(location_name)
     #View function for the navbar
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html',{"images":images,"locations":locations,"categories":categories})  
