# Generated by Django 5.0.2 on 2024-08-06 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appback', '0015_investmentterm_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentterm',
            name='video',
            field=models.URLField(blank=True, null=True),
        ),
    ]
