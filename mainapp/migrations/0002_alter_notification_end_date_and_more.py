# Generated by Django 4.1 on 2022-09-11 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='notification',
            name='from_date',
            field=models.DateTimeField(),
        ),
    ]
