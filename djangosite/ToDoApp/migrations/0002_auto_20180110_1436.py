# Generated by Django 2.0.1 on 2018-01-10 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todotask',
            name='date_finished',
            field=models.DateTimeField(verbose_name='date finished'),
        ),
    ]
