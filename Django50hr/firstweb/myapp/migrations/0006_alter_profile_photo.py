# Generated by Django 3.2.13 on 2022-05-17 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='userprofiledefault.png', null=True, upload_to='photoprofile'),
        ),
    ]
