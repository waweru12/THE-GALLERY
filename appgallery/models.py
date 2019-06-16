from django.db import models
import datetime as dt


# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to = 'appgallery/', default='DEFAULT VALUE')
    ima_name = models.CharField(max_length=33)
    ima_description = models.TextField()
    location = models.ForeignKey(location)
    category = models.ForeignKey(category)
    article_image = models.ImageField(upload_to = 'appgallery')
    post_date = models.DateTimeField(default=2)


    def __str__ (self):
      return self.ima_name

    def save_Image(self):
      self.save()

    def delete_image(self):
       self.delete()



    @classmethod
    def get_image_by_id(cls,id):
        image_result = cls.objects.get(id=id)
        return image_result
    @classmethod
    def get_all_images(cls):
        all_images = Image.objects.all()
        for image in all_images:
            return image
    
    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__icontains=search_term)
        return images

    @classmethod
    def get_with_location(cls,location):
        images = cls.objects.filter(location__location_name__icontains=location)
        return images

    @classmethod
    def get_with_category(cls,category):
        images = cls.objects.filter(category__category_name__icontains=category)
        return images
    @classmethod
    def get_single_image(cls,image_name):
        image = cls.objects.filter(image_name__icontains=image_name)
        return image
    @classmethod
    def update_image(cls,current,new):
        to_update = Image.objects.filter(image_name=current).update(image_name=new)
        return to_update

    @classmethod
    def search_by_category(cls,search_term):
        images = cls.objects.filter(category__category_name__icontains=search_term)
        return images
        
    class Meta:
        ordering = ['ima_name']



class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name
    
    def save_location(self):
        self.save()



class Category(models.Model):

    category_name = models.CharField(max_length=30)

    def __str__(self):
        return self.category_name
    
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
        


