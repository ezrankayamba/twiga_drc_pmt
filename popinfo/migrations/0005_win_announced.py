# Generated by Django 2.2.7 on 2020-01-07 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('popinfo', '0004_auto_20200106_2027'),
    ]

    operations = [
        migrations.AddField(
            model_name='win',
            name='announced',
            field=models.BooleanField(default=False),
        ),
    ]
