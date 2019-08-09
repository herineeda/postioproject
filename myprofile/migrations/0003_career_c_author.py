# Generated by Django 2.1.10 on 2019-08-08 12:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myprofile', '0002_auto_20190808_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='career',
            name='c_author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_career', to=settings.AUTH_USER_MODEL),
        ),
    ]