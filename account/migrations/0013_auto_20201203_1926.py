# Generated by Django 3.1.2 on 2020-12-03 18:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20201203_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Work as',
            new_name='Job',
        ),
    ]
