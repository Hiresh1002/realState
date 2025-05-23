from django.db import models

# Create your models here.
class Patient_signup(models.Model):
    First_name=models.CharField(max_length=50)
    Last_name=models.CharField(max_length=50)
    Contact_number=models.CharField(max_length=50)
    Email_iD=models.CharField(max_length=254)



    