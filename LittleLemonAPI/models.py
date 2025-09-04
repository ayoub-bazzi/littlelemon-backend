from django.db import models
from django.conf import settings

class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self):
        return f"{self.title} - {self.price}"

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_time = models.TimeField()
    party_size = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.booking_date} {self.booking_time} ({self.party_size})"
