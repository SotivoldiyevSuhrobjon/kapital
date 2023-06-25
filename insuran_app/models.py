from django.db import models
# forms.py
from django.utils.translation import gettext_lazy as _


# Create your models here.
class Sugurta(models.Model):
    image = models.FileField(upload_to='images/')
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    link_page = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Sugurtalar'

    def __str__(self):
        return self.title


class Support(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    description = models.TextField()

    class Meta:
        verbose_name_plural = 'Savollar'

    def __str__(self):
        return self.name


class Social(models.Model):
    instagram = models.CharField(max_length=50, blank=True, null=True,)
    facebook = models.CharField(max_length=50, blank=True, null=True)
    youtube = models.CharField(max_length=50, blank=True, null=True)
    telegram = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Social media'


class Region(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Region'

    def __str__(self) -> str:
        return self.name


class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'City'

    def __str__(self) -> str:
        return self.name


class Sport(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Sport'

    def __str__(self) -> str:
        return self.name


class RelatedSport(models.Model):
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Sport list'

    def __str__(self) -> str:
        return self.name
