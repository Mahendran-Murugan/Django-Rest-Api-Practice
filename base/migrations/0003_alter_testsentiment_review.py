# Generated by Django 5.0.3 on 2024-03-17 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_testsentiment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsentiment',
            name='review',
            field=models.TextField(blank=True, null=True),
        ),
    ]