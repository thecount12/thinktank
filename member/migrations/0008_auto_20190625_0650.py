# Generated by Django 2.2.2 on 2019-06-25 06:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20190625_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberpackage',
            name='package_name',
            field=models.CharField(blank=True, max_length=60),
        ),
        migrations.AlterField(
            model_name='membership',
            name='package_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.MemberPackage'),
        ),
    ]
