# Generated by Django 2.2.7 on 2019-12-03 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('setups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('status', models.CharField(default='INT', max_length=10)),
                ('municipal', models.CharField(max_length=40, null=True)),
                ('town', models.CharField(max_length=40, null=True)),
                ('duration', models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Duration(Years)')),
                ('authority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Authority')),
                ('consultant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Consultant')),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Region')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='setups.Type')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSupplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=1, max_digits=10, verbose_name='Price(TZS)')),
                ('remarks', models.CharField(max_length=255, verbose_name='Specific Requirement')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_suppliers', to='projects.Project')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_suppliers', to='setups.Supplier')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectFinancer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('financer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_financers', to='setups.Financer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_financers', to='projects.Project')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectContractor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_contractor', models.BooleanField(default=False)),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_contractors', to='setups.Contractor')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_contractors', to='projects.Project')),
            ],
        ),
    ]
