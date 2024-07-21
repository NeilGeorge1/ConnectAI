# Generated by Django 5.0.6 on 2024-07-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='personality_questions',
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='avatars/'),
        ),
    ]