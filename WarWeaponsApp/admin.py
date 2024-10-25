from django.contrib import admin
from WarWeaponsApp.models import Weapon

# Register your models here.
class WeaponAdmin(admin.ModelAdmin):
    list_display = ['Weapon_Name',
                    'Weapon_Type',
                    'Weapon_Slot',
                    'Critical_Utility',
                    'CriticalDMG_Utility',
                    'Status_Utility'
        ]

admin.site.register(Weapon,WeaponAdmin)