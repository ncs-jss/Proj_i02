from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class departments(models.Model):
    department = models.CharField(max_length=10)

    class Meta:
        verbose_name = _("Department")

    def __str__(self):
        return self.department


class storage_locations(models.Model):
    location = models.CharField(max_length=30)
    department = models.ForeignKey(departments, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Locations")

    def __str__(self):
        return self.location


class inventory(models.Model):
    item = models.CharField(max_length=50)
    item_total_count = models.IntegerField(default=0)
    item_department = models.ForeignKey(departments, on_delete=models.CASCADE)

    def __str__(self):
        return self.item


class count_division(models.Model):
    item_name = models.ForeignKey(inventory, on_delete=models.CASCADE)
    location = models.ForeignKey(storage_locations, on_delete=models.CASCADE)
    item_count = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("DividedCount")

    def __str__(self):
        return self.item_name
