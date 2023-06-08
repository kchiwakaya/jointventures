# Generated by Django 4.1.5 on 2023-06-03 15:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('farmersapp', '0002_alter_farmer_othername'),
    ]

    operations = [
        migrations.CreateModel(
            name='Farm',
            fields=[
                ('farm_name', models.CharField(max_length=500)),
                ('plot_number', models.CharField(blank=True, max_length=250, null=True)),
                ('extend', models.DecimalField(decimal_places=4, max_digits=10)),
                ('district', models.CharField(max_length=20)),
                ('province', models.CharField(max_length=250)),
                ('ward', models.CharField(blank=True, max_length=10, null=True)),
                ('tenure_type', models.CharField(max_length=50)),
                ('water_availability', models.CharField(max_length=250)),
                ('id', models.UUIDField(default=uuid.uuid1, editable=False, primary_key=True, serialize=False, unique=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmersapp.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Venture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripiton', models.TextField()),
                ('supporting_images', models.CharField(max_length=250)),
                ('amount', models.DecimalField(decimal_places=4, max_digits=20)),
                ('farm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmersapp.farm')),
            ],
        ),
    ]