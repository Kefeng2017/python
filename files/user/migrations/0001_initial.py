# Generated by Django 2.1.3 on 2019-01-06 22:44

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('manager', models.CharField(max_length=100)),
                ('size', models.IntegerField(default=0, null=True)),
                ('description', models.TextField(null=True)),
                ('class_code', models.CharField(max_length=6, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.CharField(max_length=255, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('f_time', models.DateTimeField(null=True)),
                ('manager_id', models.CharField(max_length=100)),
                ('full', models.IntegerField(default=0, null=True)),
                ('done', models.IntegerField(default=0, null=True)),
                ('description', models.TextField(null=True)),
                ('example', models.FileField(null=True, upload_to=user.models.get_folder)),
                ('class_id', models.CharField(max_length=100)),
                ('finished', models.CharField(default=0, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=11, null=True)),
                ('belong', models.CharField(max_length=100, null=True)),
                ('class_id', models.CharField(max_length=100, null=True)),
                ('ip', models.CharField(max_length=20, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('role', models.CharField(default='student', max_length=10, null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.CharField(max_length=255, null=True)),
                ('author_id', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('f_time', models.DateTimeField(null=True)),
                ('mission_id', models.CharField(max_length=10)),
                ('description', models.TextField(null=True)),
                ('files', models.FileField(upload_to=user.models.get_folder)),
                ('onload', models.CharField(default=0, max_length=1)),
                ('class_id', models.CharField(max_length=100)),
            ],
        ),
    ]