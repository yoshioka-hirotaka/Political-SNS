# Generated by Django 5.1.3 on 2024-11-27 15:36

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('politicians', '0005_rename_question_politician_election_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
            preserve_default=False,
        ),
    ]
