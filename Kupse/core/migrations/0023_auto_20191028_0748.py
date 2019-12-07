# Generated by Django 2.2 on 2019-10-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_item_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')], max_length=3),
        ),
        migrations.AlterField(
            model_name='item',
            name='slug',
            field=models.SlugField(),
        ),
    ]
