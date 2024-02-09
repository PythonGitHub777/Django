# Generated by Django 5.0.1 on 2024-02-02 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/'),
        ),
        migrations.AddField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]