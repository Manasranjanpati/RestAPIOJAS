# Generated by Django 3.2.2 on 2021-05-08 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetData',
            fields=[
                ('asset_no', models.IntegerField(primary_key=True, serialize=False)),
                ('asset_name', models.CharField(max_length=100)),
                ('asset_price', models.FloatField()),
                ('asset_quantity', models.IntegerField()),
            ],
        ),
    ]