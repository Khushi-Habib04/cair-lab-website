# Generated by Django 5.0.6 on 2024-05-21 05:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0007_remove_faculty_id_alter_faculty_faculty_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Student",
            fields=[
                ("Student_id", models.AutoField(primary_key=True, serialize=False)),
                ("Student_name", models.CharField(default="", max_length=100)),
                ("Student_roll_no", models.CharField(default="", max_length=20)),
                (
                    "Student_image",
                    models.ImageField(default="", upload_to="students/images"),
                ),
                ("Student_phone_no", models.CharField(default="", max_length=15)),
                ("Rid", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Publications",
            fields=[
                ("Publication_id", models.AutoField(primary_key=True, serialize=False)),
                ("Publication_name", models.CharField(default="", max_length=255)),
                (
                    "Publication_scopus",
                    models.BooleanField(
                        choices=[(True, "Yes"), (False, "No")], default=False
                    ),
                ),
                (
                    "Publication_quartile",
                    models.CharField(
                        choices=[
                            ("Q1", "Q1"),
                            ("Q2", "Q2"),
                            ("Q3", "Q3"),
                            ("Q4", "Q4"),
                        ],
                        default="Q1",
                        max_length=2,
                    ),
                ),
                (
                    "Publication_pdf",
                    models.FileField(default="", upload_to="publications/pdfs"),
                ),
                (
                    "Faculty_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.faculty"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RU",
            fields=[
                ("RU_id", models.AutoField(primary_key=True, serialize=False)),
                ("RU_domain", models.CharField(default="", max_length=255)),
                ("RU_pdf", models.FileField(default="", upload_to="ru/pdfs")),
                (
                    "Faculty_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.faculty"
                    ),
                ),
                (
                    "Student_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="home.student"
                    ),
                ),
            ],
        ),
    ]
