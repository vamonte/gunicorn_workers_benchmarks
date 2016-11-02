from __future__ import unicode_literals
from django.db import models


# Create your models here.


class E(models.Model):
    n = models.PositiveIntegerField(default=0)


class D(models.Model):
    e = models.ForeignKey(E, related_name="d")


class C(models.Model):
    d = models.ForeignKey(D, related_name="c")


class B(models.Model):
    c = models.ForeignKey(C, related_name="b")


class A(models.Model):
    b = models.ForeignKey(B, related_name="a")

