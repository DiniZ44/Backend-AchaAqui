# Generated by Django 3.1.1 on 2020-10-05 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_empresa_premium'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='descricao',
            field=models.CharField(max_length=50),
        ),
    ]
