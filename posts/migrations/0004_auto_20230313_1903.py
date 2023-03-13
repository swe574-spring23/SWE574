# Generated by Django 3.2.18 on 2023-03-13 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaces', '__first__'),
        ('posts', '0003_auto_20230312_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='spaces',
            field=models.ManyToManyField(blank=True, related_name='posts', to='spaces.Space'),
        ),
        migrations.DeleteModel(
            name='Space',
        ),
    ]