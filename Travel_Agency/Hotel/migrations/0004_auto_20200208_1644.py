# Generated by Django 3.0.2 on 2020-02-08 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hotel', '0003_auto_20200205_0016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hotel',
            old_name='childern',
            new_name='children',
        ),
    ]