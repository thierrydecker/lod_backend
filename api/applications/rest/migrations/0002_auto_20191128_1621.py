# Generated by Django 2.2.7 on 2019-11-28 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='related_workspace',
            new_name='related_parent',
        ),
    ]