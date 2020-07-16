from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db.models.signals import post_save

app_name='core'




# Create your models here.
class Journal(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    slug = models.SlugField(unique=True)

    content = models.TextField()
    image = models.ImageField(upload_to='blogpost_files/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('core:journal-detail', kwargs={'slug': self.slug})    

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type    
    


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pic/', blank=True, null='True')
    passion = models.TextField(default='Passionate')
    location = models.CharField(max_length=50, default='World')
    about_me = models.TextField(default='About me')
    plan = models.TextField()


    def __str__ (self):
        return self.user.username





class   CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id=obj_id).filter(parent=None)
        #comments = Comment.objects.filter(content_type=content_type, object_id=obj_id)
        return qs


class Comment(models.Model):
    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    #journal = models.ForeignKey(Journal, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey("self",on_delete=models.CASCADE, null=True, blank=True)

    content = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.user.username



    def children(self):
        return Comment.objects.filter(parent=self) 

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True    
           

class Foll(models.Model):
    user      = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='is_following', blank=True)
    #following = models.ManyToManyField(User, related_name='following', blank=True)
    activated = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username

def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Foll.objects.get_or_create(user=instance)
        default_user_profile = Foll.objects.get_or_create(user__id=1)[0]
        default_user_profile.followers.add(instance)
        #default_user_profile.save()
        profile.followers.add(default_user_profile.user)
        profile.followers.add(2)


post_save.connect(post_save_user_receiver, sender=User)




