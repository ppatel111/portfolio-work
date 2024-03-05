# Generated by Django 5.0.1 on 2024-01-19 19:07

import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('about_id', models.UUIDField(db_column='about_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('about_us', models.TextField(db_column='about_us')),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('modified_on', models.DateTimeField(auto_now=True, db_column='modified_on')),
            ],
            options={
                'verbose_name_plural': 'About Us',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('user_id', models.UUIDField(db_column='user_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('email', models.EmailField(db_column='email', max_length=255, unique=True)),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('joined_on', models.DateTimeField(auto_now_add=True, db_column='joined_on')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('collection_id', models.UUIDField(db_column='collection_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('collection_name', models.CharField(db_column='collection_name', max_length=255)),
                ('file_table_name', models.CharField(blank=True, db_column='file_table_name', max_length=255, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, db_column='created_on')),
                ('status', models.CharField(db_column='status', default='in_progress', max_length=255)),
                ('user', models.ForeignKey(db_column='user', on_delete=django.db.models.deletion.CASCADE, related_name='collections', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('campaign_id', models.UUIDField(db_column='campaign_id', default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('campaign_name', models.CharField(db_column='campaign_name', max_length=255)),
                ('start_date', models.DateTimeField(db_column='start_date')),
                ('end_date', models.DateTimeField(db_column='end_date')),
                ('collection', models.ForeignKey(db_column='collection', on_delete=django.db.models.deletion.CASCADE, related_name='campaigns', to='api.collection')),
            ],
        ),
    ]