from django.db import models
from django.urls import reverse
# from decimal import Decimal
# from django.utils.translation import ugettext_lazy as _


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=120)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(max_length=120, unique=True)

    def __str__(self):
        return self.name


class Unit(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Document(models.Model):
    date_of_purchase = models.DateField(blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    total = models.DecimalField(
        decimal_places=2, max_digits=7, blank=True, null=True)

    def __str__(self):
        return str(self.date_of_purchase) + " | " + str(self.location)

    def get_absolute_url(self, *args, **kwargs):
        return reverse('index', kwargs={'doc_id': self.pk})


class Position(models.Model):
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.ForeignKey(
        Unit, on_delete=models.CASCADE, default=1, null=True)
    quantity = models.DecimalField(decimal_places=2, max_digits=6)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    total = models.DecimalField(
        decimal_places=2, max_digits=8, blank=True, null=True)  # will be calculated

    # def __str__(self):
    #     return self.product

    # def total(self):
    #     total = Decimal(str(self.count * self.price_unit))
    #     return total.quantize(Decimal('0.01'))
