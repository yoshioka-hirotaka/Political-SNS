# Generated by Django 5.1.3 on 2024-11-27 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('politicians', '0006_result_pub_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='politician_name',
            new_name='politician',
        ),
    ]