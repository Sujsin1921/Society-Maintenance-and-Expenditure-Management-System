# Generated by Django 3.1.5 on 2021-04-08 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210407_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='members',
            name='mode',
            field=models.CharField(default='monthly', max_length=20),
            preserve_default=False,
        ),
    ]
