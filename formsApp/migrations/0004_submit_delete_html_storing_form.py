# Generated by Django 4.1.7 on 2023-06-13 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("formsApp", "0003_rename_form_data_form_form"),
    ]

    operations = [
        migrations.CreateModel(
            name="Submit",
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
                ("submit_data", models.JSONField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "form_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="formsApp.form"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="HTML_storing_form",
        ),
    ]