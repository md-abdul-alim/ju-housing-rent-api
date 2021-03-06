# Generated by Django 4.0.5 on 2022-06-19 09:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('renter', '0001_initial'),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='unit',
            old_name='tenant',
            new_name='renter',
        ),
        migrations.RemoveField(
            model_name='houseowner',
            name='address',
        ),
        migrations.AlterUniqueTogether(
            name='unit',
            unique_together={('name', 'renter')},
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
