# Generated by Django 3.0.2 on 2020-02-03 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0005_auto_20200203_2218'),
    ]

    operations = [
        migrations.CreateModel(
            name='CV',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
                ('curriculum', models.ImageField(blank=True, upload_to='')),
            ],
        ),
    ]
