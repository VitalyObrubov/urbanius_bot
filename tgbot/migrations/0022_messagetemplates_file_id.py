# Generated by Django 4.0.6 on 2022-08-18 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0021_messagestosend_file_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='messagetemplates',
            name='file_id',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='file_id'),
        ),
    ]
