# Generated by Django 4.0.4 on 2022-06-27 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0004_rename_vehicle_type1_vehicle_type_vehicle_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle_type',
            name='name',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]
