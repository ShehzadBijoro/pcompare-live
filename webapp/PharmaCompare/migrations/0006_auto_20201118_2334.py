# Generated by Django 3.1.3 on 2020-11-18 18:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PharmaCompare', '0005_auto_20201118_2333'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='descriptiion',
            new_name='description',
        ),
    ]