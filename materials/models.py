from django.db import models


class Material(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(blank=True)
    time_published = models.DateTimeField(auto_now_add=True)
