from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, pre_delete
from django.dispatch.dispatcher import receiver


 



class Profile(models.Model):
    expression = models.CharField(max_length=10000,blank=True,default='')
    result = models.CharField(max_length=10000,blank=True,default='')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.expression



class Password_Table(models.Model): 
    password = models.CharField(max_length=10000,blank=True,default='')
    user = models.OneToOneField(User,on_delete=models.CASCADE)
   




# @receiver(pre_delete, sender=User)
# def create_profile(sender, instance, *args, **kwargs):
#     Profile(user=User)
        


 