# Generated by Django 2.2.16 on 2020-10-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("response", "0016_actions_auto_created_date")]

    operations = [
        migrations.AddField(
            model_name="externaluser",
            name="deleted",
            field=models.BooleanField(default=False),
        )
    ]
