# Generated by Django 4.0.3 on 2022-05-03 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0002_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='campaign',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='history.campaign'),
        ),
    ]
