# Generated by Django 4.0.5 on 2022-06-23 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_alter_user_birthday'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmergencyContactPerson',
            new_name='EmergencyContact',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='family_members',
            new_name='family_member',
        ),
    ]
