# Generated by Django 4.1.7 on 2023-03-03 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon1', '0004_products_image_alter_products_privacy'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='photos/images'),
        ),
    ]