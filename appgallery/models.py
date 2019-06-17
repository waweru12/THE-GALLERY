from django.db import models
import datetime as dt


# Create your models here.



class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name
    
    def save_location(self):
        self.save()


    
    @classmethod
    def get_location(cls):
        locations = cls.objects.all()
        return locations
      
    @classmethod
    def get_with_location(cls):
        images = cls.objects.filter(location_name__icontains=location)
        return images



class Category(models.Model):

    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        



    @classmethod
    def get_with_category(cls,category):
        images = cls.objects.filter(Category__category_name__icontains=category)
        return images
        

class Image(models.Model):
    image = models.ImageField(upload_to = 'appgallery/')
    ima_name = models.CharField(max_length=33)
    ima_description = models.TextField()
    location=models.ForeignKey(Location,blank=True,default=4)
    category=models.ForeignKey(Category)
   
    def search_by_category(self,search_term):
        images = self.objects.filter(category = search_term)
        return images

    def __str__ (self):
      return self.ima_name

    def save_Image(self):
      self.save()

    def delete_image(self):
       self.delete()



    
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        for image in all_images:
            return image

    @classmethod
    def get_image_by_id(cls,id):
        image_result = cls.objects.get(id=id)
        return image_result

            
    
    @classmethod
    def get_single_image(cls,ima_name):
        image = cls.objects.filter(ima_name__icontains=ima_name)
        return image
    @classmethod
    def update_image(cls,current,new):
        to_update = Image.objects.filter(ima_name=current).update(ima_name=new)
        return to_update

    class Meta:
        ordering = ['ima_name']



