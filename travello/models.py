from django.db import models

# Create your models here.
class Destination(models.Model):
  title = models.CharField(max_length = 100)
  image = models.ImageField(upload_to = 'images')
  subtitle = models.TextField()
  price = models.IntegerField()