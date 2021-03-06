# Generated by Django 2.0.5 on 2018-05-25 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Author', models.CharField(blank=True, max_length=20)),
                ('Time', models.DateTimeField(auto_now=True)),
                ('Content', models.TextField(max_length=10000)),
                ('Quantity', models.PositiveIntegerField(default=0)),
                ('Show', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='Course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='Article', to='app.Course'),
        ),
    ]
