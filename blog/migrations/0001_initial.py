# Generated by Django 3.0 on 2020-07-29 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=50, unique=True)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
            ],
        ),
    ]
