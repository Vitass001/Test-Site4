# Generated by Django 3.2.7 on 2023-03-08 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0019_remove_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('A', 'Hik'), ('B', 'Viotek'), ('C', 'Hanwha')], default=1, max_length=50),
            preserve_default=False,
        ),
    ]
