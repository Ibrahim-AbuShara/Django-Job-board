# Generated by Django 3.2.7 on 2021-09-13 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_jobs_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='Gander',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female'), ('male/female', 'male/female')], default='', max_length=20),
            preserve_default=False,
        ),
    ]