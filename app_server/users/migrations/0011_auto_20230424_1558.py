# Generated by Django 3.2.18 on 2023-04-24 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_badge_userbadge'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbadge',
            name='badge',
        ),
        migrations.RemoveField(
            model_name='userbadge',
            name='user',
        ),
        migrations.DeleteModel(
            name='Badge',
        ),
        migrations.DeleteModel(
            name='UserBadge',
        ),
    ]
