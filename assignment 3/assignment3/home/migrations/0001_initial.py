# Generated by Django 3.0.8 on 2020-07-21 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=50)),
            ],
        ),
    ]
