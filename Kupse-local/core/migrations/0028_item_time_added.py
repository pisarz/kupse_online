# Generated by Django 2.2 on 2019-10-28 11:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20191028_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='time_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]