# Generated by Django 5.1.3 on 2024-11-21 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question_text1',
        ),
    ]
