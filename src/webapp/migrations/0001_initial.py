# Generated by Django 5.0.6 on 2024-06-09 08:27

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='E-mail')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('login', models.CharField(max_length=50, unique=True, verbose_name='Логин')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность уч. записи')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Является персоналом')),
            ],
            options={
                'verbose_name': 'ПОЛЬЗОВАТЕЛЬ',
                'verbose_name_plural': 'ПОЛЬЗОВАТЕЛИ',
                'db_table': 'Пользователи',
                'ordering': ['-created_at'],
            },
        ),
    ]