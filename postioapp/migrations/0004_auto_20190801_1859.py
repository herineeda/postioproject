# Generated by Django 2.1.10 on 2019-08-01 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postioapp', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
