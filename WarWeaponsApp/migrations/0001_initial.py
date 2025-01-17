# Generated by Django 3.2 on 2024-10-25 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weapon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Weapon_Name', models.CharField(max_length=255)),
                ('Weapon_Type', models.CharField(choices=[('CLOSE RANGE', 'close range'), ('MID RANGE', 'mid range'), ('LONG RANGE', 'long range')], max_length=50)),
                ('Weapon_Slot', models.CharField(choices=[('PRIMARY', 'primary'), ('SECONDARY', 'secondary'), ('MELEE', 'melee')], max_length=50)),
                ('Critical_Utility', models.FloatField()),
                ('CriticalDMG_Utility', models.FloatField()),
                ('Status_Utility', models.FloatField()),
            ],
        ),
    ]
