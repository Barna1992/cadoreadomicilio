# Generated by Django 3.0.4 on 2020-04-01 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locali', '0003_auto_20200401_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locale',
            name='orario_mattina',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='locale',
            name='orario_pomeriggio',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
