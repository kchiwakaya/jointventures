# Generated by Django 4.1.5 on 2023-06-18 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='irrigation',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=250, null=True),
        ),
    ]
