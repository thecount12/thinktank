# Generated by Django 2.2.2 on 2019-06-25 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0009_auto_20190625_2257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='monthly_rate',
        ),
    ]
