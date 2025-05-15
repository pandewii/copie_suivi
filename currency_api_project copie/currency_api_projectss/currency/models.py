from django.db import models

class TNDconv(models.Model):
    date = models.DateField()
    eur = models.DecimalField(max_digits=10, decimal_places=4)
    usd = models.DecimalField(max_digits=10, decimal_places=4)

class DZDconv(models.Model):
    date = models.DateField()
    tnd = models.DecimalField(max_digits=10, decimal_places=4)
    eur = models.DecimalField(max_digits=10, decimal_places=4)
    usd = models.DecimalField(max_digits=10, decimal_places=4)
