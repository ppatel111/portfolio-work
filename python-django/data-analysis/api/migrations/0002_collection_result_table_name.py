# Generated by Django 5.0.1 on 2024-01-19 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='result_table_name',
            field=models.CharField(blank=True, db_column='result_table_name', max_length=255, null=True),
        ),
    ]
