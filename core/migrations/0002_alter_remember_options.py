# Generated by Django 4.2.1 on 2023-05-30 00:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remember',
            options={'verbose_name': 'Воспоминание', 'verbose_name_plural': 'Воспоминания'},
        ),
    ]