from django.db import models


# Create your models here.
class charityapp(models.Model):
    reg_number = models.CharField(max_length=30)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=70)
    volunteer = models.CharField(max_length=10)
    location = models.CharField(max_length=100)

    class Meta:
        db_table = "charity"
