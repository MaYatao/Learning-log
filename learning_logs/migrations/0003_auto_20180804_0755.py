# Generated by Django 2.1 on 2018-08-04 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_add',
            new_name='date_added',
        ),
    ]
