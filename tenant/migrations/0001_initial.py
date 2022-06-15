# Generated by Django 4.0.5 on 2022-06-15 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_by', models.CharField(max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('created_from', models.CharField(max_length=255, null=True)),
                ('modified_by', models.CharField(max_length=255, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('modified_from', models.CharField(max_length=255, null=True)),
                ('is_archived', models.BooleanField(default=False)),
                ('archived_by', models.CharField(max_length=255, null=True)),
                ('archived_at', models.DateTimeField(null=True)),
                ('archived_from', models.CharField(max_length=255, null=True)),
                ('reason_of_house_change', models.TextField(blank=True, null=True)),
                ('rent_of_date', models.DateField(blank=True, null=True)),
                ('present_house_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='present_house_owner', to='account.commonusermodel')),
                ('previous_house_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='previous_house_owner', to='account.commonusermodel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.commonusermodel')),
            ],
            options={
                'verbose_name': 'Tenant',
                'verbose_name_plural': 'Tenants',
                'db_table': 'tenant',
                'ordering': ['-created_at'],
            },
        ),
    ]