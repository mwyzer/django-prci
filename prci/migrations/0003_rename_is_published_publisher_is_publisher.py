# Generated by Django 4.2.7 on 2023-11-30 06:01

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prci", "0002_publisher_is_published"),
    ]

    operations = [
        migrations.RenameField(
            model_name="publisher",
            old_name="is_published",
            new_name="is_publisher",
        ),
    ]
