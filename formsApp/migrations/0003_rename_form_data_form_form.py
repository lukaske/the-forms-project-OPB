# Generated by Django 4.1.7 on 2023-06-13 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("formsApp", "0002_form"),
    ]

    operations = [
        migrations.RenameField(
            model_name="form",
            old_name="form_data",
            new_name="form",
        ),
    ]
