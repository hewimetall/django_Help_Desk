# Generated by Django 3.0.2 on 2020-01-25 13:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('label_ListPage', '0002_auto_20200124_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='dashbourdbd',
            name='manager_a',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    related_name='manager_aCr', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='dashbourdbd',
            name='priority',
            field=models.IntegerField(blank=True, choices=[(1, 'Низкий'), (2, 'Нормальный'), (3, 'Срочный')], default=1,
                                      null=True),
        ),
        migrations.AlterField(
            model_name='dashbourdbd',
            name='status',
            field=models.IntegerField(
                choices=[(1, 'В обработке'), (2, 'Отправленно на доработку'), (3, 'В работе'), (4, 'Выполнена'),
                         (5, 'Закрыта')], default=1),
        ),
    ]
