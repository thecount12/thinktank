# Generated by Django 2.2.2 on 2019-06-26 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0015_userbill_package_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbill',
            name='package_name',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mpkg', to='member.MemberPackage'),
        ),
    ]
