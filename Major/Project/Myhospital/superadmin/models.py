from django.db import models

class Superadmin_data(models.Model):
    name = models.CharField(max_length=50)
    psw = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    # def __str__(self):
    #     return self.psw
