# Generated by Django 4.1.3 on 2022-11-20 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_profile_location_profile_skill_profile_skill_desc_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]
