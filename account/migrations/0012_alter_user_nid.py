# Generated by Django 4.0.5 on 2022-07-18 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_user_nid_back_image_user_nid_font_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
