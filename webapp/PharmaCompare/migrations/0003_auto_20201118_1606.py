# Generated by Django 3.1.3 on 2020-11-18 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PharmaCompare', '0002_auto_20201118_1559'),
    ]

    operations = [
        migrations.RenameField(
            model_name='generic',
            old_name='gen_name',
            new_name='g_name',
        ),
    ]
