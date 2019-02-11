# Generated by Django 2.1.5 on 2019-02-07 02:17

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('ftpcafeperfeito', '0003_auto_20190206_2201'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent',
                 mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                            related_name='children', to='ftpcafeperfeito.Genre')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='menu',
            name='tn_parent',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]