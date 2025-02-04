# Generated by Django 5.1.3 on 2024-12-15 14:14

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("pet", "0002_testimonial_rating"),
    ]

    operations = [
        migrations.CreateModel(
            name="GetinTouch",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("subject", models.CharField(blank=True, max_length=255, null=True)),
                ("message", models.TextField(blank=True, null=True)),
                ("submitted_at", models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                "verbose_name": "GetinTouch",
                "verbose_name_plural": "GetinTouchs",
                "ordering": ["-created_at", "-updated_at"],
            },
        ),
    ]
