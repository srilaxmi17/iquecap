# Generated by Django 5.0.2 on 2024-10-05 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appback', '0020_rename_file_url_investmentdeliverable_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='feeds',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('v_title', models.CharField(max_length=225)),
                ('v_description', models.TextField()),
                ('v_url', models.URLField(blank=True, null=True)),
            ],
        ),
    ]