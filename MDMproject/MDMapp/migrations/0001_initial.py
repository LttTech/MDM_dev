# Generated by Django 3.2 on 2021-04-23 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCapture',
            fields=[
                ('name', models.CharField(max_length=20, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('employee_number', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('department', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CellphoneCapture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_manufacturer', models.CharField(max_length=10)),
                ('phone_model', models.CharField(max_length=10)),
                ('imei_number', models.IntegerField()),
                ('sim_number', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='MDMapp.usercapture')),
            ],
        ),
    ]