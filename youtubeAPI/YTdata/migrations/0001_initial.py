# Generated by Django 3.2.15 on 2022-09-27 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_id', models.CharField(max_length=250)),
                ('video_title', models.CharField(max_length=300, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('published_datetime', models.DateTimeField()),
                ('thumbnail_urls', models.URLField()),
                ('channel_id', models.CharField(max_length=500)),
                ('channel_title', models.CharField(max_length=500)),
            ],
        ),
    ]
