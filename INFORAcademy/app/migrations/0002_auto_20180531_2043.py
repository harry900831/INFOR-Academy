# Generated by Django 2.0.5 on 2018-05-31 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='Time',
            field=models.DateField(auto_now=True),
        ),
    ]