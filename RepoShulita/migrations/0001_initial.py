# Generated by Django 2.1.3 on 2018-12-19 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Boleta',
            fields=[
                ('idBoleta', models.AutoField(primary_key=True, serialize=False)),
                ('nroPedido', models.IntegerField()),
                ('fecha', models.DateField()),
                ('fechaEntrega', models.DateField()),
                ('estado', models.CharField(max_length=15)),
                ('total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('idPersona', models.AutoField(primary_key=True, serialize=False)),
                ('run', models.CharField(max_length=10, unique=True)),
                ('nombreCompleto', models.CharField(max_length=100)),
                ('fechaNacimiento', models.DateField()),
                ('telefono', models.IntegerField(null=True)),
                ('direccion', models.CharField(max_length=254)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=25)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('foto', models.ImageField(blank=True, upload_to='media')),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='boleta',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RepoShulita.Persona'),
        ),
        migrations.AddField(
            model_name='boleta',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='RepoShulita.Producto'),
        ),
    ]