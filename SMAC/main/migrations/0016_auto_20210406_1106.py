# Generated by Django 3.1.5 on 2021-04-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20210403_1903'),
    ]

    operations = [
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.CharField(max_length=20)),
                ('this_month_collection', models.CharField(max_length=20)),
                ('expence', models.CharField(max_length=20)),
                ('this_month_expence', models.CharField(max_length=20)),
                ('balance', models.CharField(max_length=20)),
            ],
        ),
        
        migrations.AlterField(
            model_name='members',
            name='join_date',
            field=models.CharField(max_length=20),
        ),
    ]