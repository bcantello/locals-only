from django.db import models
from apps.authentication.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # This doesn't create a new time field. Instead it updates the field created in the previous line.

    def __str__(self):
        return self.name


class Activity(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='activities', on_delete=models.CASCADE)

    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    details = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name

