from django.contrib.auth.models import User
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    name = models.CharField(max_length=30)
    price = models.FloatField()
    specifications = models.TextField()
    description = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    image = models.ImageField(upload_to='post_images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

class Order(models.Model):
    item = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity = models.IntegerField()
    total_cost = models.FloatField()
    customer_name = models.CharField(max_length=20)
    phone = models.CharField(max_length=30)

    def __str__(self):
        return str(self.item)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Todo(models.Model):
    task = models.CharField(max_length=255)
    data = models.DateField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.task