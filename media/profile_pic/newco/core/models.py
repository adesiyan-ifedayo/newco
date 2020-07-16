from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Journal(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='blogpost_files', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/profile_pic', blank=True)
    passion = models.TextField(default='Passionate')
    location = models.CharField(max_length=50, default='World')
    about_me = models.TextField(default='About me')


    def __str__ (self):
        return self.user.username

