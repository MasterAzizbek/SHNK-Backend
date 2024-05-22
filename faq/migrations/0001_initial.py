# Generated by Django 5.0.4 on 2024-05-21 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FaqModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faq_title_en', models.CharField(max_length=500)),
                ('faq_title_uz', models.CharField(max_length=500)),
                ('faq_content_en', models.TextField()),
                ('faq_content_uz', models.TextField()),
            ],
        ),
    ]
