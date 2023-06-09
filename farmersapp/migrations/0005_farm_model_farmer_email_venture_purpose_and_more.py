# Generated by Django 4.1.5 on 2023-06-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmersapp', '0004_farm_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='model',
            field=models.CharField(blank=True, choices=[('A1', 'A1'), ('A2', 'A2'), ('Old', 'Old Resettlement Scheme'), ('Sma', 'Small Scale Commercial'), ('A1T', 'Three Tier'), ('Comm', 'Communal')], max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='farmer',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='venture',
            name='purpose',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='farm',
            name='tenure_type',
            field=models.CharField(choices=[('Off', 'Offer Letter'), ('99', '99-Year Lease'), ('A1', 'A1 Permit'), ('AP', 'A1 Temporal Permit'), ('A2', 'A2 Permit'), ('Ttl', 'Title Deed'), ('DG', 'Deed of Grant'), ('CCT', 'Certificate of Consolidated Title'), ('Non', 'None')], max_length=50),
        ),
    ]
