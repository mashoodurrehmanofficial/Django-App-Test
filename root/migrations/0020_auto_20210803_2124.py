# Generated by Django 3.2.4 on 2021-08-03 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0019_alter_classlist_uid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='is_allowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='teacher',
            name='uid',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='classlist',
            name='student',
            field=models.ManyToManyField(blank=True, to='root.Student'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='class_list',
            field=models.ManyToManyField(blank=True, to='root.ClassList'),
        ),
        migrations.AlterField(
            model_name='standard',
            name='subject_list',
            field=models.ManyToManyField(blank=True, to='root.Subject'),
        ),
    ]
