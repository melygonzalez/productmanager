# Generated by Django 4.2 on 2023-05-08 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_product_status_alter_productimage_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(to='products.category'),
        ),
        migrations.DeleteModel(
            name='ProductCategory',
        ),
    ]