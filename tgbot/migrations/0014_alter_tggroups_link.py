# Generated by Django 4.0.6 on 2022-08-12 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0013_user_verified_by_security_alter_offers_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tggroups',
            name='link',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ссылка на группу'),
        ),
    ]