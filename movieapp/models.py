from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField(max_length=1000)
    img = models.ImageField(upload_to='gallery')
    year=models.IntegerField()

    def __str__(self):
      return self.name