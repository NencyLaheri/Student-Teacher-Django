# Generated by Django 4.1 on 2022-08-18 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_applicationmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationmodel',
            name='status',
            field=models.CharField(choices=[('none', 'none'), ('accepted', 'accepted'), ('rejected', 'rejected')], default='none', max_length=20),
        ),
    ]
