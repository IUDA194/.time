from django.db import models

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    reg_data = models.DateField()

class User_Data(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField()

class Timer_Ssesion(models.Model):
    id = models.IntegerField(primary_key=True)
    datatime_start = models.DateTimeField()
    timer_time = models.IntegerField()
    name = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
