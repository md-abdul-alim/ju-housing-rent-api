# Generated by Django 4.0.5 on 2022-07-02 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0017_rename_check_in_permission_unit_check_in_permission_nid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='check_in_permission_nid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
