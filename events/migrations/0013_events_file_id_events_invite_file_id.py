# Generated by Django 4.0.6 on 2022-08-17 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_eventrequests_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='file_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='file_id'),
        ),
        migrations.AddField(
            model_name='events',
            name='invite_file_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='file_id'),
        ),
    ]
