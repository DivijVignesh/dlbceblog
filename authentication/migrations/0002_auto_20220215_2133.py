# Generated by Django 3.2.6 on 2022-02-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.AddField(
            model_name='account',
            name='phoneno',
            field=models.CharField(default='900009', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='rollno',
            field=models.CharField(default='3201364100', max_length=50),
        ),
        migrations.AddField(
            model_name='account',
            name='yearofjoining',
            field=models.CharField(default='2020-2024', max_length=50),
        ),
    ]