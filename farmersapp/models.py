from django.db import models
import uuid

# Create your models here.
class Farmer(models.Model):
    name = models.CharField(max_length=250)
    othername = models.CharField(max_length=250,null=True, blank=True)
    surname = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=250)
    gender = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    id = models.UUIDField(default=uuid.uuid1,unique=True,primary_key=True,editable=False)

    def __str__(self):
     return self.name +" "+ self.surname