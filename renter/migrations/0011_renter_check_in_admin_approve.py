# Generated by Django 4.0.5 on 2022-07-16 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('renter', '0010_renter_check_out_admin_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='renter',
            name='check_in_admin_approve',
            field=models.BooleanField(default=False),
        ),
    ]