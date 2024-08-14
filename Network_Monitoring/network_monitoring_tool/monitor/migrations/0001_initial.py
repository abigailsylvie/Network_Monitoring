# Generated by Django 5.0.7 on 2024-07-30 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vulnerability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('port', models.IntegerField()),
                ('service', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=50)),
            ],
        ),
    ]
