# Generated by Django 3.2.12 on 2023-02-27 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon1', '0002_alter_products_description_alter_products_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='privacy',
            field=models.CharField(choices=[('1', 'public'), ('2', 'private')], max_length=2, null=True,blank=True),
        ),
    ]
