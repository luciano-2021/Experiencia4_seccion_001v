# Generated by Django 3.2.3 on 2021-07-07 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tipomaterial',
            fields=[
                ('idtipo', models.IntegerField(primary_key=True, serialize=False, verbose_name='id tipo identificacion')),
                ('descripcion', models.CharField(max_length=20, verbose_name='descripcion')),
            ],
        ),
        migrations.CreateModel(
            name='Proveedores',
            fields=[
                ('ididentificacion', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id identificacion')),
                ('nombrecompleto', models.CharField(max_length=50, verbose_name='Nombre completo')),
                ('Telefono', models.CharField(max_length=150, verbose_name='Telefono')),
                ('direccion', models.CharField(max_length=150, verbose_name='direccion')),
                ('email', models.CharField(max_length=150, verbose_name='email')),
                ('pais', models.CharField(max_length=150, verbose_name='pais')),
                ('monedadepago', models.CharField(max_length=150, verbose_name='monedadepago')),
                ('tipomaterial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.tipomaterial')),
            ],
        ),
    ]
