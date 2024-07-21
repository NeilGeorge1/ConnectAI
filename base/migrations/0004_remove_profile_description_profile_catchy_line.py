# Generated by Django 5.0.6 on 2024-07-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_remove_profile_personality_questions_profile_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='description',
        ),
        migrations.AddField(
            model_name='profile',
            name='catchy_line',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
