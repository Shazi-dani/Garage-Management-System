# Generated by Django 5.0.6 on 2024-07-20 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]