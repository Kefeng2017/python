# Generated by Django 2.1.3 on 2019-01-07 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, null=True)),
                ('c_time', models.DateTimeField(auto_now_add=True)),
                ('last_mess', models.TextField(null=True)),
            ],
        ),
    ]
