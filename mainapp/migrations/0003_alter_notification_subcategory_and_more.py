# Generated by Django 4.1 on 2022-09-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_notification_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='SubCategory',
            field=models.CharField(choices=[('army', 'army'), ('navy', 'navy'), ('airforce', 'Inter'), ('airforce', 'airforce'), ('paramilitary', 'paramilitary'), ('other', 'other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='notification',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='notification',
            name='from_date',
            field=models.DateField(),
        ),
    ]
