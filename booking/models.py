from django.db import models
# Create your models here.


class register(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    nem_password = models.BigIntegerField(max_length=12)
    confirm_password = models.BigIntegerField(max_length=12)

    def __str__(self):
        return self.username
