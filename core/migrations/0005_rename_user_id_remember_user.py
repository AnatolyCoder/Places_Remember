# Generated by Django 4.2.1 on 2023-05-30 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_rename_user_remember_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remember',
            old_name='user_id',
            new_name='user',
        ),
    ]
