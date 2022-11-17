# Generated by Django 4.1.3 on 2022-11-15 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_userbookrelation_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbookrelation',
            name='rate',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Ok'), (2, 'Fine'), (3, 'Good'), (4, 'Amazing'), (5, 'Incredible')], null=True, verbose_name='Оценка'),
        ),
    ]
