# Generated by Django 4.0.5 on 2022-06-19 09:22

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
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
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
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
                ('owner_status', models.BooleanField(default=False)),
                ('renter_status', models.BooleanField(default=False)),
                ('admin_status', models.BooleanField(default=False)),
                ('account_complete_status', models.BooleanField(default=False)),
                ('cleaner', models.ManyToManyField(blank=True, related_name='cleaners', to='account.othermembers')),
                ('driver', models.ManyToManyField(blank=True, related_name='drivers', to='account.othermembers')),
                ('emergency_contact', models.ManyToManyField(blank=True, related_name='emergency_contacts', to='account.emergencycontactperson')),
                ('family_members', models.ManyToManyField(blank=True, related_name='family_members', to='account.familymembers')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('married_status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.marriedstatus')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
                'db_table': 'user',
                'ordering': ['-created_at'],
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
