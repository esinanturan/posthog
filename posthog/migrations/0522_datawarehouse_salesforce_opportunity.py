# Generated by Django 4.2.15 on 2024-11-25 02:41
from django.db import migrations, connection


def insert_salesforce_opportunity_schemas(apps, schema_editor):
    with connection.cursor() as cursor:
        cursor.execute("SELECT id, team_id FROM posthog_externaldatasource where source_type = 'Salesforce'")
        salesforce_sources = cursor.fetchall()

    ExternalDataSchema = apps.get_model("posthog", "ExternalDataSchema")
    for source in salesforce_sources:
        schema = ExternalDataSchema.objects.create(
            name="Opportunity",
            source_id=source[0],
            team_id=source[1],
            should_sync=False,
            sync_type=None,
            sync_type_config={},
        )
        schema.save()


def reverse(apps, _):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("posthog", "0521_alter_errortrackingstackframe_context"),
    ]

    operations = [
        migrations.RunPython(insert_salesforce_opportunity_schemas, reverse),
    ]
