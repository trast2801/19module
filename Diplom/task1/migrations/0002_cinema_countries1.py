# Generated by Django 4.2.15 on 2024-08-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='countries1',
            field=models.CharField(default=' ', max_length=40),
        ),
    ]