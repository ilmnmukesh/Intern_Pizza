from djongo import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class PizzaType(models.Model):
    TYPE=(("Regular", "Regular"), ("Square", "Squaure"))
    name = models.CharField(max_length=50, choices=TYPE)
    addPrice = models.FloatField()

    class Meta:
        abstract = True

class PizzaSize(models.Model):
    SIZE = (
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large")
    )
    size = models.CharField(max_length=50, choices=SIZE)
    addPrice = models.FloatField()

    class Meta:
        abstract = True

class Topping(models.Model):
    name = models.CharField(max_length=255)
    addPrice = models.FloatField()

    def __str__(self) -> str:
        return self.name

    def to_dict(self):
        return {
            "id":self.pk,
            "name":self.name,
            "addPrice":self.addPrice
        }

class Pizza(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=255)
    price = models.FloatField()
    type = models.ArrayField(
        model_container=PizzaType
    )
    size = models.ArrayField(
        model_container=PizzaSize
    )
    defaultTopping = models.ArrayReferenceField(
        to= Topping,
        related_name="topping",
    )    
    veg = models.BooleanField(default=True)
    def __str__(self) -> str:
        return self.name


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)