# Generated by Django 4.0.5 on 2022-06-30 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0013_remove_unit_remark_unit_check_in_status_and_more'),
        ('renter', '0003_checkinout'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CheckInOut',
            new_name='CheckIn',
        ),
        migrations.AlterModelOptions(
            name='checkin',
            options={'ordering': ['-created_at'], 'verbose_name': 'Check In', 'verbose_name_plural': 'Check Ins'},
        ),
        migrations.AlterModelTable(
            name='checkin',
            table='checkin',
        ),
    ]
