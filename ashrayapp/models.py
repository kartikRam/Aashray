from django.db import models
from django.contrib.auth.models import User

class circular(models.Model):
    
    title = models.CharField(max_length = 200)
    description = models.TextField()
    timeline = models.CharField(max_length=50)
    image = models.ImageField(blank=True,null=True)
    day = models.CharField(max_length=50,default='Mon')
    date = models.CharField(max_length=50,default=20)
    author = models.CharField(max_length=50,default='qw')

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 

class profile_phil(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    image = models.ImageField(blank=True,null=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    interest = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    donations = models.CharField(max_length=150,null=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url 
