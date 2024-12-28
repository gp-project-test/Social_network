from django.db import models
from django.core.validators import RegexValidator, MinLengthValidator

# Create your models here.
phone_validator = RegexValidator(regex=r'^09\d{9}$', message='phone number must in: 111111111 form')
class Users(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    ip = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(validators=[phone_validator], max_length=11)

class Posts(models.Model):
    pass

class comments(models.Model):
    pass

class Directs(models.Model):
    pass
