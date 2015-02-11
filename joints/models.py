from django.db import models

# Create your models here.
class Joint(models.Model):
    #name=models.CharField()
    email=models.EmailField()
    

    def __unicode__(self):
        return "%s" %(self.email)
  

