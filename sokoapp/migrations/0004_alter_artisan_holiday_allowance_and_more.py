# Generated by Django 4.1.5 on 2023-01-27 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sokoapp', '0003_alter_artisan_marital_status_alter_artisan_religion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artisan',
            name='holiday_allowance',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='id_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='artisan',
            name='working_hours',
            field=models.IntegerField(default=0),
        ),
    ]
