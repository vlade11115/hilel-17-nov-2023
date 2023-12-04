from django.db import models


# Create your models here.


class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)


class QRCode(models.Model):
    text = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to="qr_codes", blank=True)
