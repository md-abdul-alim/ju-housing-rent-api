# Generated by Django 4.0.5 on 2022-06-30 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0012_unit_remark_alter_unit_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='remark',
        ),
        migrations.AddField(
            model_name='unit',
            name='check_in_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='unit',
            name='check_out_status',
            field=models.BooleanField(default=False),
        ),
    ]
