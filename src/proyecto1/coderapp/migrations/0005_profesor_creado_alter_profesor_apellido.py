# Generated by Django 5.0 on 2023-12-22 00:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coderapp", "0004_alter_profesor_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profesor",
            name="creado",
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name="profesor",
            name="apellido",
            field=models.CharField(max_length=30, null=True),
        ),
    ]
