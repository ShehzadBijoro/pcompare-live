# Generated by Django 3.1.3 on 2020-11-18 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PharmaCompare', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='drug',
            name='desc',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='drug',
            name='drug_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='drug',
            name='type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='generic',
            name='cure_for',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='generic',
            name='gen_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.FloatField(blank=True, default=9.99),
        ),
    ]
