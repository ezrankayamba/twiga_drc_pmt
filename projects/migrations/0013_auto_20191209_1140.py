# Generated by Django 2.2.7 on 2019-12-09 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('setups', '0002_district'),
        ('projects', '0012_auto_20191207_1632'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='consultant',
        ),
        migrations.AlterField(
            model_name='projectcontractor',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contractors', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='projectfinancer',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='financers', to='projects.Project'),
        ),
        migrations.AlterField(
            model_name='projectsupplier',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to='projects.Project'),
        ),
        migrations.CreateModel(
            name='ProjectConsultant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Consultant')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultants', to='projects.Project')),
            ],
        ),
    ]
