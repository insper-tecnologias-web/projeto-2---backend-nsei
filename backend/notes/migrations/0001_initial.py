# Generated by Django 3.2.18 on 2023-05-09 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('img', models.CharField(max_length=200)),
                ('ano', models.CharField(max_length=200)),
            ],
        ),
    ]
