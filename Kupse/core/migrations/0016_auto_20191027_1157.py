# Generated by Django 2.2 on 2019-10-27 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=2),
        ),
    ]
