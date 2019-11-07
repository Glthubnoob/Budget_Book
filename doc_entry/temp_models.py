from django.db import models


class Programmer(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    programmer = models.ForeignKey(Programmer, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
