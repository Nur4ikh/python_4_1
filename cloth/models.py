from django.db import models



'''Клиент'''


class Customer(models.Model):
    name = models.CharField('Имя заказчика', max_length=100)
    phone_number = models.CharField('Номер тел:', max_length=13)

    class Meta:
        verbose_name = 'заказчика'
        verbose_name_plural = 'Заказчики'

    def __str__(self):
        return self.name


'''Хэштеги'''


class Tag(models.Model):
    name_tag = models.CharField('Укажите хэштег', max_length=100)

    class Meta:
        verbose_name_plural = 'Хэштеги'
        verbose_name = 'хэштег'

    def __str__(self):
        return self.name_tag


'''Продукты'''


class Product(models.Model):
    title = models.CharField('Название продукта', max_length=100)
    image = models.ImageField('Добавьте фото продукта',
                              upload_to='product/')
    price = models.PositiveIntegerField('Цена')
    tag = models.ManyToManyField(Tag)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


'''Статус заказа'''


class StatusOrder(models.Model):
    STATUS = (
        ('Ожидание', 'Ожидание'),
        ('Выехал', 'Выехал'),
        ('Доставлено', 'Доставлено')
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'Статус'

    def __str__(self):
        return self.status

