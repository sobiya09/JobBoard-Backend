# Generated by Django 5.1.4 on 2025-01-12 04:09

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cv',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.job'),
        ),
        migrations.AlterField(
            model_name='cv',
            name='submitted_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
