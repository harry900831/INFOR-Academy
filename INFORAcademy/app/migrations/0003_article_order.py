# Generated by Django 2.0.5 on 2018-05-22 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_article_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='Order',
            field=models.PositiveIntegerField(default=7122),
        ),
    ]