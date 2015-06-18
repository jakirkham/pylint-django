"""
Ensures that django models without a __unicode__ method are flagged
"""
#  pylint: disable=C0111

from django.db import models


def external_unicode_func(model):
    return model.something


class SomeModel(models.Model):
    something = models.CharField(max_length=255)
    __str__ = external_unicode_func
