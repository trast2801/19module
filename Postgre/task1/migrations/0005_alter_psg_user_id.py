# Generated by Django 4.2.15 on 2024-08-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task1', '0004_psg_user_psg_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psg_user',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]