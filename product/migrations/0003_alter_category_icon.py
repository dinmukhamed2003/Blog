# Generated by Django 4.2.3 on 2023-07-20 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]