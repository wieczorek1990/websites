# Generated by Django 3.1.3 on 2020-11-26 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='websitecategory',
            name='count',
        ),
    ]
