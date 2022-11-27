from django.core.validators import MinValueValidator
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=32, unique=True, db_index=True)
    bank_name = models.CharField(max_length=64, blank=True, null=True)
    bank_number = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.bank_name} {self.bank_number})"


class ItemGroup(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Item(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=256)
    price = models.FloatField(default=0.0, validators=[MinValueValidator(0.00)])
    group = models.ForeignKey("ItemGroup", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} (P{float(self.price):.2f})"


class ItemPerson(models.Model):
    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    paid_by = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="items_paid_for")
    pay_to = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="items_to_pay")
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ["-item__created"]
        unique_together = ["item", "paid_by", "pay_to"]
