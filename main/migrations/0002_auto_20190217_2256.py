# Generated by Django 2.1.7 on 2019-02-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Blog',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='Header',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='ImgURL',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='SubTitile',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
