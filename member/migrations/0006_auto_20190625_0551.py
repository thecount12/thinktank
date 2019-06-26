# Generated by Django 2.2.2 on 2019-06-25 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20190625_0447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='package_name',
        ),
        migrations.AddField(
            model_name='membership',
            name='member_package',
            field=models.ManyToManyField(to='member.MemberPackage'),
        ),
    ]