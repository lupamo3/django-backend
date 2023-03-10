# Generated by Django 4.1.5 on 2023-01-26 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                ("name", models.CharField(max_length=255)),
                ("currencies", models.CharField(max_length=255)),
                ("languages", models.CharField(max_length=255)),
                ("timezones", models.CharField(max_length=255)),
                (
                    "country_code",
                    models.CharField(max_length=10, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employee",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                (
                    "job_title",
                    models.CharField(default="Software Engineer", max_length=255),
                ),
                ("company", models.CharField(default="Soko", max_length=255)),
                ("country_name", models.CharField(blank=True, max_length=255)),
                ("country_currency", models.CharField(blank=True, max_length=255)),
                ("country_language", models.CharField(blank=True, max_length=255)),
                ("country_timezone", models.CharField(blank=True, max_length=255)),
                ("employee_identifier", models.CharField(blank=True, max_length=255)),
                ("region", models.CharField(max_length=255)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employees",
                        to="sokoapp.country",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Artisan",
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
                ("first_name", models.CharField(max_length=255)),
                ("last_name", models.CharField(max_length=255)),
                ("date_of_birth", models.DateField()),
                ("holiday_allowance", models.IntegerField()),
                (
                    "marital_status",
                    models.CharField(
                        choices=[("S", "Single"), ("M", "Married")],
                        default="S",
                        max_length=2,
                    ),
                ),
                ("id_number", models.IntegerField()),
                ("working_hours", models.IntegerField()),
                ("number_of_children", models.IntegerField(default=0)),
                (
                    "religion",
                    models.CharField(
                        choices=[("C", "Christian"), ("M", "Muslim")],
                        default="C",
                        max_length=2,
                    ),
                ),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="artisans",
                        to="sokoapp.country",
                    ),
                ),
            ],
        ),
    ]
