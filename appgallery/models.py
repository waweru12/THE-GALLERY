from django.db import models

# Create your models here.
class Image(models.Model):
    ima_name = models.CharField(max_length=33)
    ima_description = models.TextField()
    # location = models.ForeignKey(location)
    # category = models.ForeignKey(category)
    article_image = models.ImageField(upload_to = 'appgallery')


    def __str__ (self):
      return self.ima_name

    def save_Image(self):
      self.save()

    def delete_image(self):
       self.delete()



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
        


