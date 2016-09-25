from django.db import models

# Create your models here.

'''
class Querykeys(models.Model):
    busid = models.CharField(max_length=10)
    id_number = models.CharField(max_length=20)
    name = models.CharField(max_length=12)
    mobile = models.CharField(max_length=15)
    card_number = models.CharField(max_length=30)
    device_id = models.CharField(max_length=50)
'''

class queryapply(models.Model):
    busid = models.CharField(max_length=10)
    token = models.CharField(max_length=50)
    usr_name = models.CharField(max_length=12)
    filepath = models.FileField(upload_to='./tmpfiles/tmp')
    usr_datetime =  models.DateTimeField(auto_now_add=True)