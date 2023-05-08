# Generated by Django 4.2 on 2023-05-08 10:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('AC', 'ACTIVE'), ('IN', 'INACTIVE')], default='AC', help_text='Enter product status', max_length=15),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='image',
            field=models.CharField(help_text='Enter product image link', max_length=150),
        ),
        migrations.AlterField(
            model_name='productimage',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]