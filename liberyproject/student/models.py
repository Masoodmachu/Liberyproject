from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Students(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    place=models.CharField(max_length=35)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name=models.CharField(max_length=25)
    subject=models.CharField(max_length=35)
    place=models.CharField(max_length=30)
    image=models.ImageField(upload_to='teacher/image',null=True,blank=True)
    pdf=models.FileField(upload_to='teacher/pdf')


    def __str__(self):
        return self.name




class CustomUser(AbstractUser):
    phone=models.ImageField(default=0)
    address=models.TextField(default="")

    def __str__(self):
        return self.username