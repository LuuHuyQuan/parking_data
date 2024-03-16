from django.db import models

# Create your models here.
class Parking_data(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length= 100)
    biensoxe = models.CharField(max_length=15)
    mobile = models.CharField(max_length=20)
    ngaygui = models.DateTimeField(auto_now_add=True)
    tinhtrang = models.CharField(max_length=50)
    thanhtoan = models.CharField(max_length=50)