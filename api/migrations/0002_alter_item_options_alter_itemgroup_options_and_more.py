# Generated by Django 4.1.3 on 2022-11-27 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ["-created"]},
        ),
        migrations.AlterModelOptions(
            name="itemgroup",
            options={"ordering": ["name"]},
        ),
        migrations.AlterModelOptions(
            name="itemperson",
            options={"ordering": ["-item__created"]},
        ),
        migrations.AlterModelOptions(
            name="person",
            options={"ordering": ["name"]},
        ),
    ]