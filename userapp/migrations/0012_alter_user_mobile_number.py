# Generated by Django 5.0.2 on 2024-10-03 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0011_user_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile_number',
            field=models.CharField(blank=True, max_length=15, null=True, unique=True),
        ),
    ]
