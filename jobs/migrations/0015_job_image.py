# Generated by Django 5.1.4 on 2025-01-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0014_alter_job_minimumqualification'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='jobsimages/'),
        ),
    ]
