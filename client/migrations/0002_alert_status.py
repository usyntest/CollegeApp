# Generated by Django 4.1.4 on 2022-12-13 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
