# Generated by Django 3.1.2 on 2020-11-17 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload_and_clean_excel', '0002_auto_20201117_0313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='gespharx_id',
            field=models.IntegerField(),
        ),
    ]
