# Generated by Django 3.2.3 on 2021-07-02 05:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0006_auto_20210701_2200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='grading',
        ),
    ]
