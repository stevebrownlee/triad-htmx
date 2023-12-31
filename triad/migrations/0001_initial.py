# Generated by Django 4.2.8 on 2023-12-20 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Artifact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField()),
                ("potency", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Level",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("number_of_wins", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Potion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField()),
                ("potency", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Spell",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("date_created", models.DateTimeField()),
                ("potency", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Word",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("word", models.CharField(max_length=255)),
                ("potency", models.IntegerField()),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.type"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("background", models.CharField(max_length=255)),
                ("sorceror_name", models.CharField(max_length=255)),
                (
                    "xp_level",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.level"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Power",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("attack_strength", models.IntegerField()),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.type"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Material",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("material", models.CharField(max_length=255)),
                ("potency", models.IntegerField()),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.type"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ingredient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("potency", models.IntegerField()),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.type"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Familiar",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("type", models.CharField(max_length=255)),
                ("potency", models.IntegerField()),
                ("date_created", models.DateTimeField()),
                (
                    "artifact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.artifact"
                    ),
                ),
                (
                    "potion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.potion"
                    ),
                ),
                (
                    "spell",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.spell"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SpellWords",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "spell",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.spell"
                    ),
                ),
                (
                    "word",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.word"
                    ),
                ),
            ],
            options={
                "unique_together": {("spell", "word")},
            },
        ),
        migrations.CreateModel(
            name="PotionIngredients",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ingredient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="triad.ingredient",
                    ),
                ),
                (
                    "potion",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.potion"
                    ),
                ),
            ],
            options={
                "unique_together": {("potion", "ingredient")},
            },
        ),
        migrations.CreateModel(
            name="FamiliarPowers",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "familiar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.familiar"
                    ),
                ),
                (
                    "power",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.power"
                    ),
                ),
            ],
            options={
                "unique_together": {("power", "familiar")},
            },
        ),
        migrations.CreateModel(
            name="ArtifactMaterials",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "artifact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.artifact"
                    ),
                ),
                (
                    "material",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="triad.material"
                    ),
                ),
            ],
            options={
                "unique_together": {("artifact", "material")},
            },
        ),
    ]
