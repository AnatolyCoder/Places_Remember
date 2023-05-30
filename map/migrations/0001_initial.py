# Generated by Django 4.2.1 on 2023-05-29 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social_django', '0011_alter_id_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Remember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя воспоминания')),
                ('comment', models.CharField(max_length=300, verbose_name='Комментарий')),
                ('lat', models.CharField(max_length=20)),
                ('lng', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_django.usersocialauth')),
            ],
        ),
    ]
