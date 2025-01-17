# Generated by Django 5.0.2 on 2024-06-29 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appback', '0003_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_images/')),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
