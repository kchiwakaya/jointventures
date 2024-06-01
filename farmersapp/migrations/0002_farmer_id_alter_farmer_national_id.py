# Generated by Django 4.1.5 on 2024-05-30 11:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farmersapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farmer',
            name='id',
            field=models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='farmer',
            name='national_id',
            field=models.CharField(max_length=30, null=True, unique=True),
        ),
    ]
