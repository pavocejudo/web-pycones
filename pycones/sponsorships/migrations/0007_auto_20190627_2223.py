# Generated by Django 2.2.2 on 2019-06-27 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("sponsorships", "0006_auto_20190619_1518")]

    operations = [
        migrations.AddField(
            model_name="sponsor",
            name="sponsor_order",
            field=models.IntegerField(
                default=0, help_text="Relative order of the sponsor"
            ),
        )
    ]

