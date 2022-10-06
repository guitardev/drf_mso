# Generated by Django 4.1.1 on 2022-10-05 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="gov_nid",
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
                ("nnid", models.CharField(max_length=20, verbose_name="nnid")),
                ("title", models.CharField(max_length=50, verbose_name="title")),
                ("f_name", models.CharField(max_length=100, verbose_name="f_name")),
                ("l_name", models.CharField(max_length=100, verbose_name="l_name")),
                (
                    "birth_date",
                    models.CharField(
                        max_length=100, null=True, verbose_name="birth_date"
                    ),
                ),
                ("sex", models.CharField(max_length=50, null=True, verbose_name="sex")),
                (
                    "body_code",
                    models.CharField(max_length=2, null=True, verbose_name="body_code"),
                ),
                (
                    "house_code",
                    models.CharField(
                        max_length=20, null=True, verbose_name="house_code"
                    ),
                ),
            ],
            options={"db_table": "gov_nid", "ordering": ["-house_code"],},
        ),
    ]
