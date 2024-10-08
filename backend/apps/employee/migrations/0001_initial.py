# Generated by Django 5.1.1 on 2024-09-23 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('profile_picture', models.ImageField(upload_to='uploads/employee/profile_picture')),
                ('designation', models.CharField(max_length=50)),
                ('facebook', models.URLField(blank=True)),
                ('instagram', models.URLField(blank=True)),
                ('twitter', models.URLField(blank=True)),
                ('linkedin', models.URLField(blank=True)),
                ('youtube', models.URLField(blank=True)),
                ('banner', models.ImageField(upload_to='uploads/employee/banner')),
                ('biography', models.TextField()),
                ('phone_number', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
