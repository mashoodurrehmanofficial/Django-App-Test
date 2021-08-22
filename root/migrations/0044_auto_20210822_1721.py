# Generated by Django 3.2.4 on 2021-08-22 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('root', '0043_remove_attendancereport_xx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expression', models.CharField(blank=True, default='', max_length=10000)),
                ('result', models.CharField(blank=True, default='', max_length=10000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='AttendanceReport',
        ),
        migrations.RemoveField(
            model_name='classlist',
            name='student',
        ),
        migrations.RemoveField(
            model_name='standard',
            name='class_list',
        ),
        migrations.RemoveField(
            model_name='standard',
            name='subject_list',
        ),
        migrations.DeleteModel(
            name='Teacher',
        ),
        migrations.RemoveField(
            model_name='teacherprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='ClassList',
        ),
        migrations.DeleteModel(
            name='Standard',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='Subject',
        ),
        migrations.DeleteModel(
            name='TeacherProfile',
        ),
    ]
