# Generated by Django 2.2.4 on 2019-09-30 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(default='About me'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/profile_pic'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(default='World', max_length=50),
        ),
        migrations.AlterField(
            model_name='profile',
            name='passion',
            field=models.TextField(default='Passionate'),
        ),
    ]
