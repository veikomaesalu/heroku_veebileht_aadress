# Generated by Django 3.1 on 2020-08-31 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
            ],
        ),
    ]
