# Generated by Django 4.0.6 on 2023-02-18 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ashrayapp', '0005_profile_phil'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile_phil',
            name='donations',
            field=models.CharField(max_length=150, null=True),
        ),
    ]