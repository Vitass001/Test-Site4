# Generated by Django 3.2.7 on 2023-04-14 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0030_alter_post_camera_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Legal_Entity',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]