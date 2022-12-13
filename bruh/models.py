from __future__ import unicode_literals
import uuid
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import validate_email
from django.db import models
from django.utils import timezone
from bruh.managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(primary_key=True, editable=False)
    email = models.EmailField(_('email address'), validators=[validate_email], unique=True)
    first_name = models.CharField(max_length=75)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, editable=False)
    is_superuser = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Admins"
        verbose_name = "Admin"


class Visitor(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    ipaddress = models.TextField(max_length=150, blank=True)
    city = models.TextField(max_length=150, blank=True)
    state = models.TextField(max_length=150, blank=True)
    country = models.TextField(max_length=150, blank=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=12, blank=True)
    zipcode = models.IntegerField(blank=True)
    when_visited = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=3000)
    when_sent = models.DateTimeField(auto_now=True)
