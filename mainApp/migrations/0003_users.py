# Generated by Django 4.0.4 on 2022-05-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_visitor'),
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('employee_id', models.IntegerField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_surname', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
