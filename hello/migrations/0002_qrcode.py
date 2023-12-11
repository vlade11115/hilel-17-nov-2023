# Generated by Django 4.2.7 on 2023-12-04 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("hello", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="QRCode",
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
                ("text", models.CharField(max_length=200)),
                ("qr_code", models.ImageField(blank=True, upload_to="qr_codes")),
            ],
        ),
    ]