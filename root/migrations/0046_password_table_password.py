# Generated by Django 3.2.4 on 2021-08-22 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0045_password_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='password_table',
            name='password',
            field=models.CharField(blank=True, default='', max_length=10000),
        ),
    ]
