from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render,redirect
from .models import Image,Location,Category


def getimages(search_term):
    values =  Image.objects.filter(category = search_term)
    return values

def get_with_location(self,search_term):
    vals = Image.objects.filter(location = search_term)
    return vals

# Create your views here.
def home(request):
    images = Image.objects.all()
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html',{'images':images,"locations":locations,"categories":categories})

def view_by_location(request,location_name):
      
    images = get_with_location(location_name)
     #View function for the navbar
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html',{"images":images,"locations":locations,"categories":categories})  

def view_by_category(request,category_name):

    images = getimages(category_name)
    #View function for the navbar
    locations = Location.objects.all()
    categories = Category.objects.all()

    return render(request, 'index.html',{'images':images,"locations":locations,"categories":categories})


def View_full_image(request,name):
    image = Image.get_single_image(name)
    #View function for the navbar
    locations = Location.objects.all()
    categories = Category.objects.all()

    return render(request,'image.html',{'image':image,"locations":locations,"categories":categories})

def search_category(request):
    #View function for the navbar
    locations = Location.objects.all()
    categories = Category.objects.all()
    search_term = request.GET.get("image")

    def getimages(search_term):
        values =  Image.objects.filter(category = search_term)
        return values 

    if search_term:
        images = getimages(search_term)
        message = f"{search_term}"
        return render(request,'searched.html',{'images':images,"locations":locations,"categories":categories})
    else:
        images = getimages(search_term)
        message = "You haven't searched for any term"
        return render(request,'searched.html',{"locations":locations,"categories":categories})