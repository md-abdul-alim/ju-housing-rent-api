# Generated by Django 4.0.5 on 2022-06-19 06:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmergencyContactPerson',
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
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=11)),
                ('relation', models.CharField(blank=True, max_length=255, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Emergency Contact Person',
                'verbose_name_plural': 'Emergency Contact Persons',
                'db_table': 'emergency_contact_person',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='FamilyMembers',
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
                ('name', models.CharField(max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('relation', models.CharField(max_length=255, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'Family Member',
                'verbose_name_plural': 'Family Members',
                'db_table': 'family_member',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='MarriedStatus',
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
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Married Status',
                'verbose_name_plural': 'Married Statuses',
                'db_table': 'married_status',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OtherMembers',
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
                ('name', models.CharField(max_length=255, null=True)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('nid', models.IntegerField()),
                ('present_address', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Other Member',
                'verbose_name_plural': 'Other Members',
                'db_table': 'other_member',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CommonUserModel',
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
                ('phone', models.CharField(max_length=11, null=True)),
                ('nid', models.IntegerField(null=True)),
                ('passport', models.CharField(blank=True, max_length=100, null=True)),
                ('present_address', models.CharField(blank=True, max_length=100, null=True)),
                ('permanent_address', models.CharField(blank=True, max_length=100, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=255, null=True)),
                ('occupation_institution', models.CharField(blank=True, max_length=255, null=True)),
                ('religion', models.CharField(blank=True, max_length=255, null=True)),
                ('education_qualification', models.CharField(blank=True, max_length=255, null=True)),
                ('account_complete_status', models.BooleanField(default=False)),
                ('driver', models.ManyToManyField(blank=True, related_name='driver', to='account.othermembers')),
                ('emergency_contact', models.ManyToManyField(blank=True, related_name='emergency_contact', to='account.emergencycontactperson')),
                ('family_members', models.ManyToManyField(blank=True, related_name='family_members', to='account.familymembers')),
                ('house_cleaner', models.ManyToManyField(blank=True, related_name='house_cleaner', to='account.othermembers')),
                ('married_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.marriedstatus')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Common User',
                'verbose_name_plural': 'Common Users',
                'db_table': 'common_user',
                'ordering': ['-created_at'],
            },
        ),
    ]
