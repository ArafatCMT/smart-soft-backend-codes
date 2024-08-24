from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(null=True, blank=True)
    image_url = models.CharField(max_length=250, blank=True, null=True, default='https://i.ibb.co/XsJCM4t/image-placeholder-icon-11.png')

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

