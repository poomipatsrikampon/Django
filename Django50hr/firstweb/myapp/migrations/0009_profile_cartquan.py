# Generated by Django 3.2.13 on 2022-05-31 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_cart_time_stamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cartquan',
            field=models.IntegerField(default=0),
        ),
    ]