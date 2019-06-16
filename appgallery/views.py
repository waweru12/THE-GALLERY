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

    