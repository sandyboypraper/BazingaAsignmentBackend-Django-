# Generated by Django 2.2.4 on 2019-08-31 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20190831_2148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='name',
        ),
        migrations.AddField(
            model_name='orders',
            name='customername',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='goto',
            field=models.URLField(default='https://www.google.com', max_length=250),
        ),
        migrations.AddField(
            model_name='orders',
            name='itemname',
            field=models.CharField(default=' ', max_length=200),
        ),
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(default='0'),
        ),
        migrations.AddField(
            model_name='orders',
            name='quantity',
            field=models.IntegerField(default='9'),
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.EmailField(blank=True, default='@gmail.com', max_length=254),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone_number',
            field=models.CharField(default='3', max_length=15),
        ),
    ]
