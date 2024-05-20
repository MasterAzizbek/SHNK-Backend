# Generated by Django 5.0.4 on 2024-05-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EditionCategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edition_cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='EditionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('edition_photo', models.ImageField(upload_to='editions')),
                ('edition_content', models.TextField()),
                ('edition_file', models.FileField(upload_to='edition_files')),
                ('edition_categories', models.ManyToManyField(to='editions.editioncategories')),
            ],
        ),
    ]
