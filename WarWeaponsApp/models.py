from django.db import models

# Create your models here.



class Weapon(models.Model):
    Weapon_Name = models.CharField(max_length=255)
    Weapon_Type = models.CharField(max_length=50)
    Weapon_Slot = models.CharField(max_length=50)
    Critical_Utility = models.IntegerField()
    CriticalDMG_Utility = models.FloatField()
    Status_Utility = models.IntegerField()