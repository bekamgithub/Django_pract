from django.db import models
# Create your models here.


class register(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    nem_password = models.BigIntegerField(max_length=12)
    confirm_password = models.BigIntegerField(max_length=12)

    def __str__(self):
        return self.username





class Booking(models.Model):
    SERVICE_TYPES = [
        ("Consultation", "Consultation"),
        ("Repair", "Repair"),
        ("Meeting", "Meeting"),
        ("Training", "Training"),
        ("Other", "Other"),
    ]

    STATUS_TYPES = [
        ("Pending", "Pending"),
        ("Approved", "Approved"),
        ("Cancelled", "Cancelled"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    service = models.CharField(max_length=20, choices=SERVICE_TYPES,default="Consultation")
    date = models.DateField()
    time = models.TimeField()
    guests = models.IntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_TYPES, default="Pending")

    def __str__(self):
        return f"{self.name} - {self.service}"
