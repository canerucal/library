# Generated by Django 4.0.4 on 2022-05-18 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='visitor',
            fields=[
                ('visitor_id', models.AutoField(primary_key=True, serialize=False)),
                ('visitor_name', models.CharField(max_length=20)),
                ('visitor_surname', models.CharField(max_length=20)),
                ('res_time', models.TimeField()),
            ],
            options={
                'db_table': 'visitor',
            },
        ),
    ]
