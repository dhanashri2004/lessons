# Generated by Django 5.0.6 on 2024-06-28 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=200)),
                ('salary', models.BigIntegerField()),
            ],
        ),
    ]
