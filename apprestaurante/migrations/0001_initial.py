# Generated by Django 3.2.6 on 2021-10-03 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('slug', models.SlugField(unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img')),
                ('estado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DNI', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=60)),
                ('celular', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Datos del cliente',
                'verbose_name_plural': 'Datos de los clientes',
            },
        ),
        migrations.CreateModel(
            name='Coordenada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitud', models.DecimalField(decimal_places=10, max_digits=12)),
                ('longitud', models.DecimalField(decimal_places=10, max_digits=13)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zona', models.CharField(max_length=100, verbose_name='Dirección')),
                ('referencia', models.CharField(max_length=255)),
                ('ciudad', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.ciudad')),
            ],
            options={
                'verbose_name': 'Dirección del cliente Delivery',
                'verbose_name_plural': 'Dirección del cliente Delivery',
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Local',
                'verbose_name_plural': 'Locales',
            },
        ),
        migrations.CreateModel(
            name='Promociones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name': 'Promociones',
                'verbose_name_plural': 'Promociones',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30, unique=True)),
                ('slug', models.SlugField(unique=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('descripcion', models.CharField(blank=True, max_length=255, null=True, verbose_name='Breve descripción del producto')),
                ('disponible', models.BooleanField(default=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='img')),
                ('stock', models.DecimalField(decimal_places=2, max_digits=6)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.categoria')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(auto_now_add=True)),
                ('descripcion', models.CharField(max_length=255, verbose_name='Productos que contiene el Pedido')),
                ('detalles', models.CharField(max_length=255, verbose_name='Gustos del cliente')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.cliente')),
                ('coordenada', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.coordenada')),
                ('direccion', models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.direccion')),
                ('local', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.local')),
                ('producto', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.producto')),
                ('promociones', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.promociones')),
            ],
        ),
        migrations.AddField(
            model_name='direccion',
            name='distrito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='apprestaurante.distrito'),
        ),
    ]
