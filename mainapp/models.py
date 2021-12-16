from django.db import models
from django.contrib.auth.models import User

class room (models.Model):
    destination = models.CharField(max_length=50, null=True)
    name      = models.CharField(max_length=50, null=True)
    price     = models.IntegerField()
    beds      = models.PositiveIntegerField()
    size      = models.IntegerField()

class room_number (models.Model):
    room_num = models.CharField(max_length=60)
    room = models.ForeignKey(room, on_delete=models.CASCADE)

class reservation (models.Model):
    customer  = models.ForeignKey(User, on_delete=models.CASCADE)
    room      = models.ForeignKey(room, on_delete=models.CASCADE)
    check_in  = models.DateField()
    check_out = models.DateField()
