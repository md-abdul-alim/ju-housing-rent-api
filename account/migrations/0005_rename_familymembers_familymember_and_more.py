# Generated by Django 4.0.5 on 2022-06-23 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_rename_emergencycontactperson_emergencycontact_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FamilyMembers',
            new_name='FamilyMember',
        ),
        migrations.RenameModel(
            old_name='OtherMembers',
            new_name='OtherMember',
        ),
    ]