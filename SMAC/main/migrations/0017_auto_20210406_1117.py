# Generated by Django 3.1.5 on 2021-04-06 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20210406_1106'),
    ]

    operations = [
        
        migrations.AlterField(
            model_name='balance',
            name='balance',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='balance',
            name='collection',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='balance',
            name='expence',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='balance',
            name='this_month_collection',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='balance',
            name='this_month_expence',
            field=models.IntegerField(),
        ),
    ]
