# Generated by Django 5.1.5 on 2025-01-28 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='title',
            new_name='todo',
        ),
    ]
