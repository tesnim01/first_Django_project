from django.db import models

# Create your models here.
class Post(models.Model): #creating a new database model called Post
    text = models.TextField()
    def __str__(self): # new
        return self.text[:50]