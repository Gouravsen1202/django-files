from django.db import models

# Create your models here.
class Bazzar(models.Model):
    emp_name=models.CharField(max_length=50)
    emp_email= models.EmailField(unique=True)
    emp_contact=models.IntegerField()
    emp_dob=models.DateField()
    emp_state=models.CharField(max_length=50)
    emp_gender=models.CharField(max_length=50)
    emp_password=models.CharField(max_length=15)

