# Generated by Django 3.2.8 on 2021-10-29 01:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kafkan_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kafkan',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kafkan', to=settings.AUTH_USER_MODEL),
        ),
    ]
