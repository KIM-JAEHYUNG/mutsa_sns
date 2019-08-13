# Generated by Django 2.0.13 on 2019-05-28 06:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0007_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_user_set',
            field=models.ManyToManyField(related_name='likes_user_set', to=settings.AUTH_USER_MODEL),
        ),
    ]
