# Generated by Django 5.0.1 on 2024-01-22 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_collection_result_table_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='result_table_name',
        ),
        migrations.AddField(
            model_name='campaign',
            name='result_table_name',
            field=models.CharField(blank=True, db_column='result_table_name', max_length=255, null=True),
        ),
    ]
