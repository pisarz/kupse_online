# Generated by Django 2.2 on 2019-10-28 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_auto_20191028_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]