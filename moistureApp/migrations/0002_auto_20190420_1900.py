# Generated by Django 2.2 on 2019-04-20 17:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moistureApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='arduino',
            old_name='arduino_name',
            new_name='name',
        ),
    ]