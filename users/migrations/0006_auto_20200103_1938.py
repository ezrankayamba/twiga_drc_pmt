# Generated by Django 2.2.7 on 2020-01-03 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200103_1808'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='roleprivilege',
            unique_together={('role', 'privilege')},
        ),
    ]
