# Generated by Django 2.2.7 on 2019-12-06 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('park', '0002_auto_20191205_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='squirrel',
            name='unique_squirrel_id',
            field=models.CharField(help_text='Unique squirrel id: Hectare+Shift+Date+Hectare Squirrel Number', max_length=32, primary_key=True, serialize=False),
        ),
    ]
