# Generated by Django 4.1.1 on 2022-10-06 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("datagov", "0002_persongov60_personhouse_delete_gov_nid_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="persongov60",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
