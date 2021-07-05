# Generated by Django 3.2.3 on 2021-05-14 15:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainer', '0002_auto_20210514_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.PROTECT, to='users.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phone',
            field=models.PositiveBigIntegerField(blank=True, null=True, unique=True),
        ),
    ]