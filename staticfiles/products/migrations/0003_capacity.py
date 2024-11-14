# Generated by Django 5.0.7 on 2024-11-08 22:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_category_slug_product_image_product_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Capacity",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.CharField(max_length=20, unique=True)),
                ("slug", models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]