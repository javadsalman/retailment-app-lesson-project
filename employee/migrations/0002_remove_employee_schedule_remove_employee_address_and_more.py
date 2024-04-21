# Generated by Django 5.0.4 on 2024-04-21 11:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='schedule',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='address',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='salary_start_date',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='full_name',
            field=models.CharField(default='Adi Isci', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='salary_day',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(default='29392035', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='EmployeeSalary',
        ),
        migrations.DeleteModel(
            name='EmployeeSchedule',
        ),
    ]