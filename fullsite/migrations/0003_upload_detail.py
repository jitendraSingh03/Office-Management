# Generated by Django 3.1 on 2021-02-08 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fullsite', '0002_connect_call'),
    ]

    operations = [
        migrations.CreateModel(
            name='upload_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('All_call', models.CharField(default='', max_length=10)),
                ('date', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
