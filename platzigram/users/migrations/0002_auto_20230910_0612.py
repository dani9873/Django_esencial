# Generated by Django 2.2 on 2023-09-10 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='modify',
            new_name='modified',
        ),
    ]