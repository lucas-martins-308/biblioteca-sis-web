# Generated by Django 5.1.7 on 2025-03-07 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255)),
                ('autor', models.CharField(max_length=255)),
                ('editora', models.CharField(max_length=255)),
                ('ano_publicacao', models.PositiveIntegerField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('disponivel', models.BooleanField(default=True)),
            ],
        ),
    ]
