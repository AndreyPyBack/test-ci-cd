from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True)
    role = models.CharField(max_length=30, default='user')
    city = models.CharField(max_length=100, blank=True)

    # def __str__(self):
    #     return self.user.username
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100, verbose_name="Марка")
    model = models.CharField(max_length=100, verbose_name="Модель")
    year = models.IntegerField(verbose_name="Год выпуска")
    color = models.CharField(max_length=50, verbose_name="Цвет")

    def __str__(self):
        return f"{self.make} {self.model} {self.year}"


from django.conf import settings
from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    full_description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()

class Comment(models.Model):
    product = models.ForeignKey(Product, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)