""" User Models"""
#django
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Profile(models.Model):
    """ Profile Model"""
    user= models.OneToOneField(User, verbose_name=("Usuario"), on_delete=models.CASCADE)
    website= models.URLField(max_length=200,blank=True)
    biography=models.TextField(blank=True)
    phone=models.CharField(max_length=20, blank=True)
    picture=models.ImageField(upload_to='users/pictures',blank=True, null=True)
    created= models.DateTimeField(auto_now_add=True)
    modified=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return self.user.username
