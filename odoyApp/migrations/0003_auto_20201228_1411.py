# Generated by Django 3.1.4 on 2020-12-28 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('odoyApp', '0002_auto_20201228_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='birth',
            field=models.DateField(verbose_name='User_birth'),
        ),
        migrations.AlterField(
            model_name='user_info',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
