# Generated by Django 2.0.3 on 2018-04-04 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_contact_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]