# Generated by Django 2.2 on 2020-02-13 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200213_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.TextField(default='블로그 챌린지'),
        ),
    ]
