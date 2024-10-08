# Generated by Django 5.0.6 on 2024-05-16 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=155)),
                ('last_name', models.CharField(max_length=155)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('orgazination', models.CharField(max_length=255)),
                ('login', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=70)),
                ('degree', models.CharField(max_length=100)),
                ('information', models.CharField(max_length=300)),
                ('avatar', models.ImageField(upload_to='avatars')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
