# Generated by Django 4.0.6 on 2022-07-06 20:40

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
                ('role_choice', models.CharField(choices=[('Пользователь', 'Пользователь'), ('менеджер', 'менеджер'), ('CRM - администратор', 'CRM - администратор')], max_length=20, verbose_name='роль')),
                ('Offer', models.BooleanField(default=False)),
                ('Avatar', models.ImageField(blank=True, upload_to='photo_sales/%Y/%m/%d', verbose_name='Аватар')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
