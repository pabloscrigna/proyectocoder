# Generated by Django 5.0 on 2023-12-19 02:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("coderapp", "0003_rename_entragado_entregable_entregado"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="profesor",
            options={"ordering": ["nombre"], "verbose_name_plural": "Profesores"},
        ),
        migrations.AlterField(
            model_name="entregable",
            name="fechaDeEntrega",
            field=models.DateField(verbose_name="Fecha de Entrega"),
        ),
    ]
