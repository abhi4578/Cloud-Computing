# Generated by Django 2.0.9 on 2018-11-29 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('phone_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=20)),
                ('date_of_birth', models.DateTimeField(null=True)),
            ],
        ),
    ]