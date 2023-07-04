# Generated by Django 4.1 on 2022-08-17 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('student', 'student'), ('faculty', 'faculty')], max_length=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
