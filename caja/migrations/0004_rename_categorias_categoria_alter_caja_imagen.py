# Generated by Django 4.2.1 on 2023-06-10 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caja', '0003_rename_categoria_categorias'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categorias',
            new_name='Categoria',
        ),
        migrations.AlterField(
            model_name='caja',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='cajafotos'),
        ),
    ]
