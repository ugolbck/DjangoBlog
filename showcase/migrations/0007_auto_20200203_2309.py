# Generated by Django 3.0.2 on 2020-02-03 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0006_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cv',
            name='curriculum',
            field=models.FileField(upload_to=''),
        ),
    ]