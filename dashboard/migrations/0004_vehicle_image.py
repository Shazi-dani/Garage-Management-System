# Generated by Django 5.0.6 on 2024-07-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_appointment_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='vehicle_images/'),
        ),
    ]
