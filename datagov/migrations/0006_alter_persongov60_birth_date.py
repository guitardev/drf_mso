# Generated by Django 4.1.1 on 2022-10-06 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "datagov",
            "0005_alter_persongov60_body_code_alter_persongov60_f_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="persongov60",
            name="birth_date",
            field=models.DateField(blank=True, null=True, verbose_name="Birthday"),
        ),
    ]