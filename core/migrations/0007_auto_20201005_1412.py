# Generated by Django 3.1.1 on 2020-10-05 17:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20201005_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='classificao',
            new_name='classificacao',
        ),
    ]
