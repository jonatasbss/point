# Generated by Django 4.0.4 on 2022-05-03 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alvo', '0004_alter_alvo_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alvo',
            name='latitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='alvo',
            name='longitude',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
