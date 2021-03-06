# Generated by Django 2.2.3 on 2019-07-04 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0002_auto_20190702_1513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devolver',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='emprestimo',
            name='nome',
        ),
        migrations.AddField(
            model_name='devolver',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='user',
            field=models.OneToOneField(default=2, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
