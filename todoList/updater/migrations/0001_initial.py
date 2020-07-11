# Generated by Django 3.0.7 on 2020-07-11 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=255)),
                ('completed', models.BooleanField()),
                ('date', models.DateField()),
            ],
        ),
    ]
