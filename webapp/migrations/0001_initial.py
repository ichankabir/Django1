# Generated by Django 3.0.5 on 2020-04-13 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('cast', models.CharField(max_length=500)),
                ('genre', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
