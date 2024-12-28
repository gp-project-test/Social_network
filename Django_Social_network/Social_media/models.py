from django.db import models

# Create your models here.

from django.db import models
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator, MinLengthValidator

# Create your models here.
phone_validator = RegexValidator(regex=r'^09\d{9}$', message='phone number must in: 111111111 form')
class Users(models.Model):
    name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
    email= models.EmailField()
    ip= models.GenericIPAddressField()
    created_at= models.DateTimeField(auto_now_add=True)
    phone_number= models.CharField(validators=[phone_validator], max_length=11)

class comments(models.Model):
    user=models.ForeignKey(Users, on_delete=models.CASCADE)
    date_comment= models.DateTimeField(auto_now_add=True)

class posts(models.Model):
    user= models.ForeignKey(Users, on_delete=models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    comment= models.ForeignKey(comments, on_delete=models.CASCADE)
class Directs(models.Model):
    pass