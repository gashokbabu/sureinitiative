# Generated by Django 3.2.3 on 2021-05-14 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='qualification',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='Qualification',
        ),
    ]