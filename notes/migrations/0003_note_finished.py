# Generated by Django 2.2.2 on 2019-06-28 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20190627_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
