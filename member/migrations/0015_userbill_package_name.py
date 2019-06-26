# Generated by Django 2.2.2 on 2019-06-26 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0014_billlineitem_userbill'),
    ]

    operations = [
        migrations.AddField(
            model_name='userbill',
            name='package_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='mpkg', to='member.MemberPackage'),
            preserve_default=False,
        ),
    ]
