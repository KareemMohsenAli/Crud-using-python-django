# Generated by Django 4.1.7 on 2023-02-27 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('amazon1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
