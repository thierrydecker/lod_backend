# Generated by Django 2.2.7 on 2019-11-28 15:18

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'parents',
            },
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('related_workspace', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest.Parent')),
            ],
            options={
                'db_table': 'childrens',
            },
        ),
    ]