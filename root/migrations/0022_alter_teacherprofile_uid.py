# Generated by Django 3.2.4 on 2021-08-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0021_auto_20210803_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherprofile',
            name='uid',
            field=models.CharField(blank=True, default='4cefbf3f-2cc4-46db-b34a-70ec2316b233', max_length=200),
        ),
    ]
