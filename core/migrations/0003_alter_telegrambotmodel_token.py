# Generated by Django 3.2 on 2021-04-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_telegrambotmodel_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegrambotmodel',
            name='token',
            field=models.CharField(max_length=46, unique=True),
        ),
    ]