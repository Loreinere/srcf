# Generated by Django 3.1.2 on 2020-12-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_profile_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First name', models.CharField(blank=True, max_length=20, null=True)),
                ('Last name', models.CharField(blank=True, max_length=20, null=True)),
                ('Work as', models.CharField(blank=True, max_length=30, null=True)),
                ('Education', models.CharField(blank=True, max_length=50, null=True)),
                ('bio', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='education',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='work as',
        ),
    ]
