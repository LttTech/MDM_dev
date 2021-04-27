from django.db import models


class UserCapture(models.Model):
    name = models.CharField(max_length=20, default=None)
    email = models.EmailField(null=True)
    employee_number = models.IntegerField(primary_key=True, unique=True)
    department = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name


class CellphoneCapture(models.Model):
    user = models.ForeignKey(UserCapture, null=True, on_delete=models.SET_NULL)
    phone_manufacturer = models.CharField(max_length=10)
    phone_model = models.CharField(max_length=50)
    imei_number = models.IntegerField()
    sim_number = models.IntegerField()
    phone_number = models.IntegerField()

    def __str__(self):
        return self.phone_model



