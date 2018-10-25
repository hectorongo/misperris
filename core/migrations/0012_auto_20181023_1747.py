# Generated by Django 2.1.2 on 2018-10-23 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20181022_1707'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('run', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_vivienda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='estado',
            name='nombre',
            field=models.CharField(max_length=20),
        ),
        migrations.AddField(
            model_name='comuna',
            name='nro_region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region', verbose_name='Región'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='comuna',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Comuna'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Region'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='tipo_vivienda',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Tipo_vivienda'),
        ),
    ]
