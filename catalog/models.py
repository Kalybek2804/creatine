from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('protein', 'Протеин'),
        ('amino_acids', 'Аминокислоты'),
        ('gainer', 'Гейнер'),
        ('vitamins', 'Витамины'),
        ('accessories', 'Аксессуары'),
    ]

    name = models.CharField(max_length=100, verbose_name='Название')
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, verbose_name='Категория')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='products/', verbose_name='Изображение')
    stock = models.PositiveIntegerField(verbose_name='Наличие на складе')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')


    def __str__(self):
        return self.name
