# Generated by Django 4.2.7 on 2023-12-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_rename_phone_studentdata_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdata',
            name='mobile',
            field=models.BigIntegerField(),
        ),
    ]
