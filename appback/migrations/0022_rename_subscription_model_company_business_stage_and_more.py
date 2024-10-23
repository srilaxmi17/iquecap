# Generated by Django 5.0.2 on 2024-10-05 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appback', '0021_feeds'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='subscription_model',
            new_name='business_stage',
        ),
        migrations.RenameField(
            model_name='company',
            old_name='type',
            new_name='bussiness_model',
        ),
        migrations.AddField(
            model_name='company',
            name='hq',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='revenue_model',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='year_founded',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='c_Benefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('benefits', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='benefits', to='appback.investmentterm')),
            ],
        ),
        migrations.CreateModel(
            name='fileurls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_f_title', models.CharField(max_length=255)),
                ('c_f_urls', models.URLField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appback.company')),
            ],
        ),
    ]
