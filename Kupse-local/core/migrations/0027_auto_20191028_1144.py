# Generated by Django 2.2 on 2019-10-28 10:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20191028_1052'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='count',
            new_name='quantity',
        ),
    ]
