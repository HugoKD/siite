# Generated by Django 4.1.3 on 2023-01-26 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactform',
            name='num',
            field=models.CharField(max_length=10),
        ),
    ]
