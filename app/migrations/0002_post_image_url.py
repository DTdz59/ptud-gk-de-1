# Generated by Django 5.1.7 on 2025-03-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
