# Generated by Django 2.2 on 2019-10-27 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_item_is_visible'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='is_visible',
            field=models.BooleanField(default=True),
        ),
    ]