# Generated by Django 3.2.5 on 2021-07-09 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='jobs.category'),
            preserve_default=False,
        ),
    ]
