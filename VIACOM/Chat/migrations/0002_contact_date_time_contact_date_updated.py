# Generated by Django 4.2.7 on 2023-11-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, default='2023-11-14 12:31:05'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
