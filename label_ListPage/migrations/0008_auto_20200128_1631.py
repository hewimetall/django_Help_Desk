# Generated by Django 3.0.2 on 2020-01-28 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('label_ListPage', '0007_auto_20200128_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='types',
            name='Types',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
