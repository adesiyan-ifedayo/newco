# Generated by Django 2.2.4 on 2019-10-03 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20191001_1325'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='plan',
            field=models.TextField(default='life'),
            preserve_default=False,
        ),
    ]
