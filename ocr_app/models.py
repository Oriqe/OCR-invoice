from django.db import models
import random
# Create your models here.





class Document(models.Model):
    docfile = models.FileField(upload_to="documents/%Y/%m/%d")

class Analyzedtext(models.Model):
    ana_text = models.TextField()
