# Generated by Django 4.1 on 2023-07-14 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="booking",
            name="no_of_guests",
            field=models.IntegerField(max_length=6),
        ),
        migrations.AlterField(
            model_name="menu",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]