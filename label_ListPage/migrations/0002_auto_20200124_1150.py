# Generated by Django 3.0.2 on 2020-01-24 11:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('label_ListPage', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketchat',
            name='name',
            field=models.ForeignKey(db_column='username', on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='userCreated', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticketchat',
            name='post',
            field=models.ForeignKey(db_column='pk', on_delete=django.db.models.deletion.CASCADE,
                                    related_name='comments', to='label_ListPage.dashBourdBd'),
        ),
        migrations.AddField(
            model_name='dashbourdbd',
            name='autors',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='autorsCr',
                                    to=settings.AUTH_USER_MODEL),
        ),
    ]
