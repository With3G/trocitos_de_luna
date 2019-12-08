# Generated by Django 3.0 on 2019-12-08 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=150, verbose_name='Cliente')),
                ('products', models.TextField(max_length=250, verbose_name='Artículos')),
                ('send', models.CharField(max_length=100, verbose_name='Método de Envío')),
                ('total', models.FloatField(verbose_name='Total')),
                ('date_buy', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'ordering': ['client'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre de la categoría')),
                ('image', models.ImageField(blank=True, upload_to='categorias/', verbose_name='Imagen de la categoría')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Listado de Categorías',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nombre de la empresa')),
                ('logo', models.ImageField(blank=True, upload_to='delivery', verbose_name='Logo de la empresa')),
                ('price', models.FloatField(verbose_name='Precio de envío')),
                ('time', models.IntegerField(verbose_name='Plazo de envío')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Envio',
                'verbose_name_plural': 'Empresas de Envío',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Design',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Diseño')),
                ('image', models.ImageField(blank=True, upload_to='design/', verbose_name='Imagen del diseño')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Diseño',
                'verbose_name_plural': 'Listado de Diseños',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Tipo de material')),
                ('image', models.ImageField(blank=True, upload_to='material/', verbose_name='Imagen del material')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Listado de Materiales',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='cliente',
            name='city',
            field=models.CharField(choices=[('ac', 'A Coruña'), ('al', 'Álava'), ('ab', 'Albacete'), ('ali', 'Alicante'), ('alm', 'Almería'), ('as', 'Asturias'), ('av', 'Ávila'), ('ba', 'Badajoz'), ('bal', 'Baleares'), ('bar', 'Barcelona'), ('bu', 'Burgos'), ('ca', 'Cáceres'), ('cad', 'Cádiz'), ('can', 'Cantabria'), ('cas', 'Castellón'), ('cr', 'Ciudad Real'), ('co', 'Córdoba'), ('cu', 'Cuenca'), ('gi', 'Girona'), ('gr', 'Granada'), ('gu', 'Guadalajara'), ('gp', 'Gipuzkoa'), ('hu', 'Huelva'), ('hues', 'Huesca'), ('ja', 'Jaén'), ('lr', 'La Rioja'), ('lp', 'Las Palmas'), ('le', 'León'), ('ler', 'Lérida'), ('lu', 'Lugo'), ('ma', 'Madrid'), ('mal', 'Málaga'), ('mu', 'Murcia'), ('na', 'Navarra'), ('ou', 'Ourense'), ('pa', 'Palencia'), ('po', 'Pontevedra'), ('sa', 'Salamanca'), ('se', 'Segovia'), ('so', 'Soria'), ('ta', 'Tarragona'), ('te', 'Santa Cruz de Tenerife'), ('ter', 'Teruel'), ('to', 'Toledo'), ('va', 'Valencia'), ('val', 'Valladolid'), ('vi', 'Vizcaya'), ('za', 'Zamora'), ('zar', 'Zaragoza')], max_length=30, verbose_name='Ciudad'),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Nombre del producto')),
                ('ref', models.IntegerField(verbose_name='Referencia')),
                ('image', models.ImageField(blank=True, upload_to='product/', verbose_name='Imagen del producto')),
                ('description', models.TextField(blank=True, verbose_name='Descripción del producto')),
                ('price', models.FloatField(verbose_name='Precio')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Category', verbose_name='Categoría')),
                ('design', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tienda.Design', verbose_name='Diseño')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Material', verbose_name='Tipo de material')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Listado de Productos',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lot', models.IntegerField(verbose_name='Cantidad')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Cliente', verbose_name='Cliente')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tienda.Product', verbose_name='Producto')),
            ],
            options={
                'verbose_name': 'Carrito',
                'verbose_name_plural': 'Carrito de la compra',
                'ordering': ['-pk'],
            },
        ),
    ]
