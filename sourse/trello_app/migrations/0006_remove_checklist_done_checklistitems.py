# Generated by Django 4.1.4 on 2022-12-17 08:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("trello_app", "0005_remove_cardmark_text_remove_checklist_not_done_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="checklist", name="done",),
        migrations.CreateModel(
            name="CheckListItems",
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
                ("done", models.BooleanField(default=False)),
                (
                    "checklist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="trello_app.checklist",
                    ),
                ),
            ],
        ),
    ]