# Generated by Django 2.2.3 on 2019-08-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('likes', '0002_auto_20190801_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='slug',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
