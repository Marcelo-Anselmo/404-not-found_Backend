# Generated by Django 5.0.3 on 2024-04-05 16:40

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("professor", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Alunos",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("nome", models.CharField(max_length=60)),
                ("curso", models.CharField(max_length=100)),
                ("RA", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "professor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="alunos",
                        to="professor.professor",
                    ),
                ),
            ],
        ),
    ]
