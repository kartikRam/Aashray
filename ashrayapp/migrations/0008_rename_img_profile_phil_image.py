# Generated by Django 4.0.6 on 2023-02-19 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ashrayapp', '0007_profile_phil_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile_phil',
            old_name='img',
            new_name='image',
        ),
    ]