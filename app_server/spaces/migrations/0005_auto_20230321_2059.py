# Generated by Django 3.1.1 on 2023-03-21 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '0004_alter_space_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='space',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
