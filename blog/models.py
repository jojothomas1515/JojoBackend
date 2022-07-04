from django.db import models

from users.models import CustomUser


# Create your models here.
class BlogPost(models.Model):
    heading = models.CharField(max_length=100, null=True, blank=True)
    cover_image = models.ImageField(default='cool.jpg')
    post_field = models.TextField(null=True, blank=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.heading
