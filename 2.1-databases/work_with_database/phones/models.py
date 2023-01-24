from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.TextField()
    release_date = models.DateField()
    lte_exists = models.CharField(max_length=5)
    slug = models.SlugField(max_length=255)



