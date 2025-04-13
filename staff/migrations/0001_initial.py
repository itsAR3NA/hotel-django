# Generated by Django 5.1.6 on 2025-04-11 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Staff",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("RCPT", "Receptionist"),
                            ("CLNR", "Cleaner"),
                            ("MGMT", "Manager"),
                            ("SVP", "Service Provider"),
                        ],
                        max_length=4,
                    ),
                ),
                ("phone_number", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("hire_date", models.DateField()),
            ],
        ),
    ]
