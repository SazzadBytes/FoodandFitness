# Generated by Django 4.1.6 on 2023-02-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BloodPresure",
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
                ("presuretype", models.CharField(max_length=100)),
                ("presuredescription", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Sugar",
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
                ("sugartype", models.CharField(max_length=100)),
                ("sugardescription", models.TextField()),
            ],
        ),
    ]