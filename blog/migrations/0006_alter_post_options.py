# Generated by Django 4.2.7 on 2024-03-06 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0005_alter_post_options_comment"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="post",
            options={"ordering": ["-posted_at", "author"]},
        ),
    ]
