# Generated by Django 3.0.3 on 2020-07-15 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erros', '0005_auto_20200715_1316'),
    ]

    operations = [
        migrations.RenameField(
            model_name='erros',
            old_name='arquiva',
            new_name='arquivar',
        ),
    ]
