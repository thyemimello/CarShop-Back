# Generated by Django 4.2.3 on 2023-07-24 18:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Car",
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
                ("brand", models.CharField(max_length=60)),
                ("model", models.CharField(max_length=120)),
                ("year", models.IntegerField(default=0, null=True)),
                ("fuel", models.CharField(max_length=20)),
                ("color", models.CharField(max_length=20)),
                ("quilometers", models.IntegerField(null=True)),
                ("price", models.IntegerField(null=True)),
                ("cover_img", models.CharField(max_length=150)),
                ("description", models.TextField(max_length=250)),
                ("is_avaliable", models.BooleanField(default=True)),
                (
                    "user_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="advertisements",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
