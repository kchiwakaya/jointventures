# Generated by Django 4.1.5 on 2024-06-01 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmersapp', '0003_alter_farmer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
