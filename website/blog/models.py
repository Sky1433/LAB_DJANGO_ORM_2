from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    is_published = models.BooleanField()
    publish_date = models.DateTimeField()