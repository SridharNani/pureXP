# Generated by Django 4.1.2 on 2022-10-24 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ticket",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("To Do", "To Do"),
                            ("In Progress", "In Progress"),
                            ("In Review", "In Review"),
                            ("Done", "Done"),
                        ],
                        default="To Do",
                        max_length=25,
                    ),
                ),
                ("description", models.TextField()),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="updated at"),
                ),
            ],
        ),
    ]
