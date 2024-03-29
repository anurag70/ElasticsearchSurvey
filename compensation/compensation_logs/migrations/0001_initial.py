# Generated by Django 3.2.17 on 2024-01-06 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompensationData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.DateField()),
                ('Age', models.IntegerField()),
                ('Industry', models.CharField(max_length=255)),
                ('JobTitle', models.CharField(max_length=255)),
                ('Salary', models.FloatField()),
                ('Currency', models.CharField(max_length=50)),
                ('Location', models.CharField(max_length=255)),
                ('Experience', models.IntegerField()),
                ('AdditionalInformation', models.TextField()),
                ('Other', models.CharField(max_length=255)),
            ],
        ),
    ]
