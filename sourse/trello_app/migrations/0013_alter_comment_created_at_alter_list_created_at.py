# Generated by Django 4.1.4 on 2022-12-21 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("trello_app", "0012_alter_board_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="list",
            name="created_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]