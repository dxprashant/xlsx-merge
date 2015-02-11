from django.db import models
import datetime

class Document(models.Model):
    docfile = models.FileField(upload_to='documents')
    date = models.DateTimeField(auto_now_add=True, blank=True)

  


