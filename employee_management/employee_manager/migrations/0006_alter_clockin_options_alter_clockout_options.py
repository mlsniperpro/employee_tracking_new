# Generated by Django 4.0.3 on 2022-03-14 13:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_manager', '0005_employeeinstance_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clockin',
            options={'ordering': ['clock_in_time']},
        ),
        migrations.AlterModelOptions(
            name='clockout',
            options={'ordering': ['clock_out_time']},
        ),
    ]
