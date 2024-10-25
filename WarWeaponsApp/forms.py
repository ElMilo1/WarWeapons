from django import forms
from django.core import validators
from WarWeaponsApp.models import Weapon
from WarWeaponsApp.models import models

class WeaponForm(forms.ModelForm):
    
    Weapon_Slot_OptionVar = [
    ('',''),
    ('PRIMARY','primary'),
    ('SECONDARY','secondary'),
    ('MELEE','melee')
    ]

    Weapon_TypeVar = [
    ('',''),
    ('CLOSE RANGE','CLOSE RANGE'),
    ('MID RANGE','MID RANGE'),
    ('LONG RANGE','LONG RANGE')
    ]

    def Percentaje_Val(x):
        if x>50 or x<0:
            raise forms.ValidationError("Ingresa un valor entre 0 y 50")
    
    Weapon_Name = forms.CharField(validators=[
        validators.MaxLengthValidator(255),
        validators.MinLengthValidator(5)
    ])
    Weapon_Type = forms.ChoiceField(choices=Weapon_TypeVar)
    Weapon_Slot = forms.ChoiceField(choices=Weapon_Slot_OptionVar)
    Critical_Utility = forms.FloatField(validators=[Percentaje_Val])
    CriticalDMG_Utility = forms.FloatField(validators=[
        validators.MinValueValidator(1),
        validators.MaxValueValidator(5)
    ])
    Status_Utility = forms.FloatField(validators=[Percentaje_Val])

    class Meta:
        model = Weapon
        fields = ['Weapon_Name','Weapon_Type','Weapon_Slot','Critical_Utility','CriticalDMG_Utility','Status_Utility']