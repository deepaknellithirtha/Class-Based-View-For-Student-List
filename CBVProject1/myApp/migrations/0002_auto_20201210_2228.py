# Generated by Django 2.2 on 2020-12-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='place',
            field=models.CharField(max_length=40),
        ),
    ]