from django.db import models

# Create your models here.


class MyUser(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    dob = models.CharField(max_length=250, null=True)
    gender = models.CharField(max_length=250, null=True, default= None, blank=True)
    issuing_authority_name = models.CharField(max_length=250)
    issuing_authority_state = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    file = models.FileField(upload_to='file/', null=True, blank=True)


