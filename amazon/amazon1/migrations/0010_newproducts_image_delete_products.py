# Generated by Django 4.1.7 on 2023-03-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon1', '0009_remove_newproducts_category_remove_newproducts_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='newproducts',
            name='image',
            field=models.ImageField(default=2, upload_to='photos/images'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Products',
        ),
    ]