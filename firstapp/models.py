from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class ClassList(models.Model):
    name = models.CharField(max_length=100,null= True, blank=True)

class Teacher(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)
    phone = models.CharField(max_length=100,blank=True,null=True)
    email = models.EmailField(max_length = 254)

class College(models.Model):
    name = models.CharField(max_length=100, null=True,blank=True)
    address = models.TextField( null=True,blank=True)
    email_id = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=100, null=True,blank=True)


class Student(AbstractUser):
    phone = models.CharField(max_length=100,blank=True,null=True)
    classlist = models.ForeignKey(ClassList,on_delete=models.CASCADE,blank=True,null=True )
    teacher = models.ForeignKey(Teacher,on_delete=models.CASCADE,blank=True,null=True )
    address= models.TextField( null=True,blank=True)

