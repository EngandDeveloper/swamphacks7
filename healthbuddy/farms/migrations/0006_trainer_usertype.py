# Generated by Django 3.1 on 2021-01-31 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farms', '0005_auto_20210131_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='userType',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
