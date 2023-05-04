from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Receipe(models.Model):
    # user = models.models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null = True, blank = True)
    receipe_name = models.CharField(max_length=100)
    receipe_description = models.TextField(max_length=200)
    receipe_image = models.ImageField(upload_to="receipe_images")
