# Generated by Django 2.2.2 on 2019-06-25 04:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('member', '0003_auto_20190624_0433'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberResources',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource_name', models.CharField(max_length=60)),
                ('resource_start', models.DateField(blank=True, null=True)),
                ('resource_end', models.DateField(blank=True, null=True)),
                ('resource_fee', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='memberpackage',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='member.MemberResources'),
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill_day', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('package_name', models.CharField(max_length=60)),
                ('member_name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='member_name', to=settings.AUTH_USER_MODEL)),
                ('paid_by', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='member_paid', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
