# Generated by Django 4.0.3 on 2022-03-21 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0005_alter_body_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='body',
            name='x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='body',
            name='y',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='body',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.body'),
        ),
    ]
