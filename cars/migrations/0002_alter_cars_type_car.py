# Generated by Django 4.2.4 on 2023-08-19 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='type_car',
            field=models.CharField(choices=[('old', 'old'), ('sport', 'sport'), ('gruz', 'gruz')], max_length=100),
        ),
    ]
