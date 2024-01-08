# Generated by Django 3.2.18 on 2023-04-21 13:59

from django.db import migrations

import nautobot.core.models.fields


class Migration(migrations.Migration):
    dependencies = [
        ("extras", "0080_tagsfield"),
        ("circuits", "0015_remove_circuittype_provider_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="circuit",
            name="tags",
            field=nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AlterField(
            model_name="circuittermination",
            name="tags",
            field=nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AlterField(
            model_name="provider",
            name="tags",
            field=nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag"),
        ),
        migrations.AlterField(
            model_name="providernetwork",
            name="tags",
            field=nautobot.core.models.fields.TagsField(through="extras.TaggedItem", to="extras.Tag"),
        ),
    ]
