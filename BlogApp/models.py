from django.db import models

# Create your models here.

class BlogTypes(models.Model):
    BlogTypeId = models.AutoField(primary_key=True)
    BlogTypeName = models.CharField(max_length=100)

class Blogs(models.Model):
    BlogId = models.AutoField(primary_key=True)
    BlogName = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    DateCreated = models.DateField()
    PhotoFileName = models.CharField(max_length=100)