# Generated by Django 5.1.2 on 2024-10-15 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('category', models.CharField(choices=[('protein', 'Протеин'), ('amino_acids', 'Аминокислоты'), ('gainer', 'Гейнер'), ('vitamins', 'Витамины'), ('accessories', 'Аксессуары')], max_length=50, verbose_name='Категория')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('description', models.TextField(verbose_name='Описание')),
                ('image', models.ImageField(upload_to='products/', verbose_name='Изображение')),
                ('stock', models.PositiveIntegerField(verbose_name='Наличие на складе')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата обновления')),
            ],
        ),
    ]
