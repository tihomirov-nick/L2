# Generated by Django 4.0.4 on 2022-11-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_notes_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='like',
            field=models.IntegerField(blank=True, default=''),
        ),
    ]
