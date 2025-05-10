from django.db import models


class Student(models.Model):
    fnm = models.CharField(max_length=100)
    lnm = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.fnm} {self.lnm}"  # Full name for uniqueness

class UserProfile(models.Model):
    fkey = models.ForeignKey(Student, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_images/')

    def __str__(self):
        return f"Profile of {self.fkey.email}"
