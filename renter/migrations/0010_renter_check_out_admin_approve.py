# Generated by Django 4.0.5 on 2022-07-16 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renter', '0009_alter_checkin_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='renter',
            name='check_out_admin_approve',
            field=models.BooleanField(default=False),
        ),
    ]
