# Generated by Django 3.0.5 on 2020-05-17 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20200517_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='note',
            field=models.TextField(),
        ),
    ]