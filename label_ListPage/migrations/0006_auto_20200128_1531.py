# Generated by Django 3.0.2 on 2020-01-28 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('label_ListPage', '0005_auto_20200128_1529'),
    ]

    operations = [
        migrations.CreateModel(
            name='Types',
            fields=[
                ('date_created', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Types', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddField(
            model_name='dashbourdbd',
            name='types',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='typesTicket', to='label_ListPage.Types'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='historicaldashbourdbd',
            name='types',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='label_ListPage.Types'),
        ),
    ]
