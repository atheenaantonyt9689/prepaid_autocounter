# Generated by Django 3.1.5 on 2021-04-23 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('billapp', '0002_auto_20210423_1921'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set(),
        ),
    ]