# Generated by Django 4.1.6 on 2023-02-09 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0006_categorysize_alter_product_size"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categoryseason",
            options={"verbose_name": "Сезоны", "verbose_name_plural": "Сезон"},
        ),
        migrations.AlterModelOptions(
            name="categorysize",
            options={"verbose_name": "Размеры", "verbose_name_plural": "Размер"},
        ),
    ]
