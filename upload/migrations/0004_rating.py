# Generated by Django 3.1.2 on 2020-12-16 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('upload', '0003_auto_20201203_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('rate', models.PositiveSmallIntegerField(choices=[(1, 'Very Bad'), (2, 'Poor'), (3, 'Ok'), (4, 'Good'), (5, 'Excellent')])),
                ('public', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='upload.upload')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rating_system', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]