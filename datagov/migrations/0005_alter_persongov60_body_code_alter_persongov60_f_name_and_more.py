# Generated by Django 4.1.1 on 2022-10-06 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "datagov",
            "0004_alter_persongov60_body_code_alter_persongov60_f_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="persongov60",
            name="body_code",
            field=models.CharField(max_length=2, null=True, verbose_name="Body_code"),
        ),
        migrations.AlterField(
            model_name="persongov60",
            name="f_name",
            field=models.CharField(max_length=200, verbose_name="Firstname"),
        ),
        migrations.AlterField(
            model_name="persongov60",
            name="l_name",
            field=models.CharField(max_length=200, verbose_name="Lastname"),
        ),
        migrations.AlterField(
            model_name="persongov60",
            name="sex",
            field=models.CharField(max_length=50, null=True, verbose_name="Sex"),
        ),
        migrations.AlterField(
            model_name="persongov60",
            name="title",
            field=models.CharField(max_length=100, verbose_name="Title"),
        ),
        migrations.AlterField(
            model_name="personhouse",
            name="house_addr",
            field=models.CharField(max_length=20, verbose_name="Houseaddr"),
        ),
        migrations.AlterField(
            model_name="personhouse",
            name="house_code",
            field=models.CharField(max_length=20, verbose_name="Housecode"),
        ),
    ]
