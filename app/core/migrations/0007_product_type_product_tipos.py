# Generated by Django 4.1.13 on 2023-12-28 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_remove_product_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='tipos',
            field=models.ManyToManyField(to='core.product_type'),
        ),
    ]
