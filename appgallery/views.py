from django.shortcuts import render
from .models import Image

# Create your views here.
def welcome(request):
    image = article_image.objects.all()
    return render(request, 'photo.html',{'image':image})