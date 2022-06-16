from django.db import models


# Create your models here.
class BlogPost(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    cover_image = models.ImageField(default='cool.jpg')
    summary = models.CharField(max_length=100, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
