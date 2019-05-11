from django.db import models
from django import forms

class Post(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=200)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)