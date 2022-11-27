# Generated by Django 4.1.3 on 2022-11-27 07:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ItemGroup",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Person",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(db_index=True, max_length=32, unique=True)),
                ("bank_name", models.CharField(blank=True, max_length=64, null=True)),
                ("bank_number", models.CharField(blank=True, max_length=16, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Item",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=256)),
                ("price", models.FloatField(validators=[django.core.validators.MinValueValidator(0.0)])),
                (
                    "group",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to="api.itemgroup"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ItemPerson",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("paid", models.BooleanField(default=False)),
                ("item", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="api.item")),
                (
                    "paid_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="items_paid_for", to="api.person"
                    ),
                ),
                (
                    "pay_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="items_to_pay", to="api.person"
                    ),
                ),
            ],
            options={
                "unique_together": {("item", "paid_by", "pay_to")},
            },
        ),
    ]