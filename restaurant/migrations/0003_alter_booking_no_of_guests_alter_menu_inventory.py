# Generated by Django 4.1 on 2023-07-14 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0002_alter_booking_id_alter_booking_no_of_guests_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="booking",
            name="no_of_guests",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="menu",
            name="inventory",
            field=models.IntegerField(),
        ),
    ]
