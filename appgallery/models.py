from django.db import models

# Create your models here.
class Image(models.Model):
    ima_name = models.CharField(max_length=33)
    ima_description = models.TextField()
    ima_location = models.ForeignKey(location)
    ima_category = models.ForeignKey(category)
    article_image = models.ImageField(upload_to = 'appgallery')


    def__str__ (self):
      return self.ima_name
               

