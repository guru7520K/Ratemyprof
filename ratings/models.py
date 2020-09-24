from django.db import models

# Create your models here.
class Rating(models.Model):
    professor = models.CharField(max_length=200)
    rating = models.IntegerField()