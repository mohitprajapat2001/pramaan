# Generated by Django 5.2 on 2025-04-15 09:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_remove_address_country_remove_address_state"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="securityquestion",
            options={
                "verbose_name": "Security Question",
                "verbose_name_plural": "Security Questions",
            },
        ),
        migrations.AlterUniqueTogether(
            name="securityquestion",
            unique_together={("user", "question")},
        ),
    ]
