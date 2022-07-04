
from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
# # Create your models here.

# class User(models.Model):
#     first_name=models.CharField(max_length=50,blank=False)
#     last_name=models.CharField(max_length=50, blank=False)
#     email=models.EmailField(max_length=50)
#     password=models.CharField(max_length=50)
#     biografia=models.TextField(blank=True)
#     birthdate=models.DateField(blank=True, null=True)
#     created=models.DateTimeField(auto_now_add=True)
#     modifi_create=models.DateTimeField(auto_now=True)
#     is_admin=models.BooleanField(default=False)

#     def __str__(self) -> str:
#         return f"{self.id} {self.first_name} | {self.email} | {self.is_admin}"
class Post(models.Model):
    """ Post Models"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profile = models.ForeignKey('users.Profile', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='posts/photos')
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    #Referencia de campos
     
    def __str__(self) -> str:
        return f" {self.title} by {self.user.user_name}"