# mainapp/models.py

from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
import os
from django.dispatch import receiver
from django.db.models.signals import post_save


def path_and_rename(instance, filename):
    upload_to = 'images/user_profile/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

# User model with additional fields for User_Type (Lawyer or Client)
class CustomUser(models.Model):
    USER_TYPES = (
        ('Lawyer', 'Lawyer'),
        ('Client', 'Client'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    bio = models.TextField(blank=True, null=True)  # Add bio field
    specialization = models.CharField(max_length=100, blank=True, null=True)  # Add specialization field
    location = models.CharField(max_length=100, blank=True, null=True)  # Add location field
    image = models.ImageField(upload_to=path_and_rename,default='images/account.png')    
    # Custom __str__ method to display the username
    def __str__(self):
        return self.user.username
    
    def delete(self, *args, **kwargs):
        super().delete(*args, **kwargs)
        if os.path.exists(self.image.url) and self.image.name != "account.png":
            os.remove(self.image.path)


@receiver(post_save, sender=User)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        CustomUser.objects.create(user=instance)
