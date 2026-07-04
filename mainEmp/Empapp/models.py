from django.db import models

class EmployeeModel(models.Model):
    Emp_Id = models.CharField(max_length=10)
    Emp_name = models.CharField(max_length=50)
    desiganation = models.CharField(max_length=40)
    salary = models.IntegerField(max_length=10)
    gender = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.Emp_name