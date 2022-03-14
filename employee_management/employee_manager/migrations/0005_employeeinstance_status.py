# Generated by Django 4.0.3 on 2022-03-14 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_manager', '0004_rename_time_clockin_clock_in_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Available'), ('b', 'Time Off')], default='a', help_text='Employee Availability', max_length=1),
        ),
    ]