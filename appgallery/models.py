from django.db import models

# Create your models here.
class Image(models.Model):
    ima_name = models.CharField(max_length=33)
    ima_description = models.TextField()
    # ima_location = models.ForeignKey(location)
    # ima_category = models.ForeignKey(category)
    article_image = models.ImageField(upload_to = 'appgallery')


    def __str__ (self):
      return self.ima_name

    def save_location(self):
      self.save()



class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def __str__(self):
        return self.location_name
    
    def save_location(self):
        self.save()



        


