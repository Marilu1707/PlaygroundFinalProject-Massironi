# Generated by Django 4.1.2 on 2022-11-13 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0002_rename_id_chat_mensaje_chat'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensaje',
            name='de_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
