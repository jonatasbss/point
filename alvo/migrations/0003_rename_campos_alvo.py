# Generated by Django 4.0.4 on 2022-05-02 02:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alvo', '0002_alter_campos_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Campos',
            new_name='Alvo',
        ),
    ]