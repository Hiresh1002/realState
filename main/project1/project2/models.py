from django.db import models

class Student(models.Model):
    fnm = models.CharField(max_length=100)
    lnm = models.CharField(max_length=100)
    email = models.EmailField(max_length=100 ,default=True) 
    password = models.CharField(max_length=100,default=True)  

    def __str__(self):
        return self.fnm
