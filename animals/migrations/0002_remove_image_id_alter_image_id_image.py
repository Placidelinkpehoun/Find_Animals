# Generated by Django 5.0.2 on 2024-08-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='id',
        ),
        migrations.AlterField(
            model_name='image',
            name='id_image',
            field=models.IntegerField(max_length=30, primary_key=True, serialize=False, unique=True),
        ),
    ]
