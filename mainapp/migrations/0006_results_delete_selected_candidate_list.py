# Generated by Django 4.1 on 2022-09-15 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_selected_candidate_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_Student', models.CharField(max_length=255)),
                ('Field_Student', models.CharField(choices=[('Defence', 'Defence'), ('Inter', 'Inter')], max_length=255)),
                ('Image_Student', models.CharField(choices=[('1', '1'), ('all', 'all')], max_length=255)),
                ('SelectedIN', models.CharField(max_length=255)),
                ('Year', models.DateField()),
                ('Slider_Img', models.ImageField(upload_to='static/media/Results/')),
            ],
        ),
        migrations.DeleteModel(
            name='Selected_candidate_list',
        ),
    ]
