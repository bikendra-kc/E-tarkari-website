# Generated by Django 3.0.5 on 2020-05-22 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20200513_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilepicture',
            name='pp',
        ),
    ]
