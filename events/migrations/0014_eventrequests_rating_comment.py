# Generated by Django 4.0.6 on 2022-08-17 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_events_file_id_events_invite_file_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventrequests',
            name='rating_comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий к оценке'),
        ),
    ]
