from django.db import models
# Create your models here.

class Post(models.Model):
    tittle=models.CharField(max_length=70)
    desc=models.TextField()

    