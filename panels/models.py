# -*- coding: utf-8 -*-
from ckeditor.fields import RichTextField
from django.db import models


# Create your models here.
class Panel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True, verbose_name="Pokój")
    number = models.CharField(max_length=255, blank=True, null=True, verbose_name="Numer")
    description = RichTextField(blank=True, null=True, verbose_name="Opis")
    faculty_description = RichTextField(blank=True, null=True, verbose_name="Wydział")

    class Meta:
        verbose_name = 'Tablica'
        verbose_name_plural = 'Tablice'

    def __str__(self):
        return '%s -> %s' % (self.title, self.number)

    def __unicode__(self):
        return self.__str__()
