# models.py

from django.db import models
from django.contrib.auth.models import User

class ExampleModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
