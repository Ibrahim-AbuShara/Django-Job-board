# Generated by Django 3.2.5 on 2021-07-09 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20210709_1955'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='description',
            field=models.TextField(default='', max_length=1500),
            preserve_default=False,
        ),
    ]
