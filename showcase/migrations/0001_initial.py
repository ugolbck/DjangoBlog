# Generated by Django 3.0.2 on 2020-02-02 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('Publication date', models.DateTimeField()),
                ('body', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
    ]
