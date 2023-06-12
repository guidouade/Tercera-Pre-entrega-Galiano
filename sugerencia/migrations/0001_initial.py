# Generated by Django 4.2.1 on 2023-06-12 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sugerencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('sugerencia', models.CharField(max_length=2000)),
            ],
            options={
                'verbose_name': 'sugerencia',
                'verbose_name_plural': 'sugerencias',
            },
        ),
    ]