# Generated by Django 3.0.2 on 2020-02-03 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_auto_20200202_2351'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='art_body',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='image',
            new_name='art_image',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='art_title',
        ),
    ]