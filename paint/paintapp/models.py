from django.db import models

# Create your models here.
class Image(models.Model):
	name=models.CharField(max_length=60)
	data=models.CharField(max_length=1000000)
