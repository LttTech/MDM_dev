# Generated by Django 3.2 on 2021-04-23 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDMapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cellphonecapture',
            name='phone_model',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='usercapture',
            name='name',
            field=models.CharField(default=None, max_length=20),
        ),
    ]