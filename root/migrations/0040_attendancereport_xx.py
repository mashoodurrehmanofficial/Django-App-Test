# Generated by Django 3.2.6 on 2021-08-20 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0039_attendancereport_submit_date_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendancereport',
            name='xx',
            field=models.CharField(blank=True, default='xx', max_length=300),
        ),
    ]
