# Generated by Django 4.2.1 on 2023-06-10 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0002_rename_categoriacaja_categoria_alter_caja_imagen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categoria',
            new_name='Categorias',
        ),
    ]
