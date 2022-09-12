# Generated by Django 4.1.1 on 2022-09-11 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test_Data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('timestamp', models.DateTimeField()),
                ('detail', models.CharField(max_length=500)),
            ],
            options={
                'db_table': 'test_data',
                'managed': False,
            },
        ),
    ]
