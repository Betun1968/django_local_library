# Generated by Django 2.1.15 on 2020-02-16 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200216_1205'),
    ]

    operations = [
        migrations.RenameField(
            model_name='languagebook',
            old_name='language',
            new_name='languagebook',
        ),
    ]
